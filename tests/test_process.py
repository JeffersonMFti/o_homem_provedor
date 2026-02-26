"""
Testes para src/process.py

Cobrem as funções de limpeza/transformação dos dados brutos do IBGE:
- limpar_renda_por_sm
- limpar_estado_conjugal
- _to_int
- _normalizar_uf
"""
import numpy as np
import pandas as pd
import pytest

from src.process import (
    _normalizar_uf,
    _to_int,
    limpar_estado_conjugal,
    limpar_renda_por_sm,
)


# ─── Helpers para construir DataFrames brutos simulados ───────────────────────

def _mock_renda_df(rows: list[dict]) -> pd.DataFrame:
    """
    Cria um DataFrame que imita a saída bruta do sidrapy para a tabela de renda.
    O primeiro row é a linha de cabeçalho (descartada por _drop_header_row).
    """
    header = {"D1N": "Unidade da Federação", "D4N": "Sexo", "D5N": "Classe SM", "V": "Valor"}
    data = [header] + rows
    return pd.DataFrame(data)


def _mock_conjugal_df(rows: list[dict]) -> pd.DataFrame:
    """
    Cria um DataFrame bruto para a tabela de estado conjugal.
    """
    header = {
        "D1N": "Unidade da Federação",
        "D4N": "Estado Conjugal",
        "D5N": "Sexo",
        "D6N": "Faixa Etária",
        "V":   "Valor",
    }
    data = [header] + rows
    return pd.DataFrame(data)


# ─── _to_int ──────────────────────────────────────────────────────────────────

class TestToInt:
    def test_converte_string_numerica(self):
        s = pd.Series(["1000", "2000", "300"])
        resultado = _to_int(s)
        assert list(resultado) == [1000, 2000, 300]

    def test_converte_traco_para_nan(self):
        s = pd.Series(["1000", "-", "500"])
        resultado = _to_int(s)
        assert resultado[0] == 1000
        assert pd.isna(resultado[1])
        assert resultado[2] == 500

    def test_converte_reticencias_para_nan(self):
        s = pd.Series(["...", "100"])
        resultado = _to_int(s)
        assert pd.isna(resultado[0])
        assert resultado[1] == 100

    def test_converte_x_para_nan(self):
        s = pd.Series(["X", "42"])
        resultado = _to_int(s)
        assert pd.isna(resultado[0])
        assert resultado[1] == 42


# ─── _normalizar_uf ───────────────────────────────────────────────────────────

class TestNormalizarUf:
    def test_title_case(self):
        s = pd.Series(["SÃO PAULO", "minas gerais"])
        resultado = _normalizar_uf(s)
        assert resultado[0] == "São Paulo"
        assert resultado[1] == "Minas Gerais"

    def test_strip_espacos(self):
        s = pd.Series(["  Rio De Janeiro  "])
        resultado = _normalizar_uf(s)
        assert resultado[0] == "Rio De Janeiro"


# ─── limpar_renda_por_sm ──────────────────────────────────────────────────────

class TestLimparRendaPorSm:
    def _df_basico(self):
        return _mock_renda_df([
            {"D1N": "São Paulo", "D4N": "Homens", "D5N": "Mais de 5 a 10 salários mínimos", "V": "50000"},
            {"D1N": "São Paulo", "D4N": "Mulheres", "D5N": "Mais de 1 a 2 salários mínimos", "V": "30000"},
        ])

    def test_remove_linha_cabecalho_sidrapy(self):
        df = self._df_basico()
        resultado = limpar_renda_por_sm(df)
        # Linha 0 do df original é o cabeçalho e deve ser descartada
        assert "Sexo" not in resultado["sexo"].values
        assert "Classe SM" not in resultado["classe_sm"].values

    def test_colunas_presentes(self):
        df = self._df_basico()
        resultado = limpar_renda_por_sm(df)
        assert set(["uf", "sexo", "classe_sm", "pessoas", "lower_brl", "upper_brl"]).issubset(
            resultado.columns
        )

    def test_pessoas_tipo_int(self):
        df = self._df_basico()
        resultado = limpar_renda_por_sm(df)
        assert resultado["pessoas"].dtype == np.int64

    def test_remove_sem_rendimento(self):
        df = _mock_renda_df([
            {"D1N": "São Paulo", "D4N": "Homens", "D5N": "Sem rendimento", "V": "10000"},
            {"D1N": "São Paulo", "D4N": "Homens", "D5N": "Mais de 1 a 2 salários mínimos", "V": "5000"},
        ])
        resultado = limpar_renda_por_sm(df)
        assert "Sem rendimento" not in resultado["classe_sm"].values
        assert len(resultado) == 1

    def test_remove_linha_total_uf(self):
        df = _mock_renda_df([
            {"D1N": "Unidade da Federação", "D4N": "Homens", "D5N": "Mais de 1 a 2 salários mínimos", "V": "999"},
            {"D1N": "São Paulo", "D4N": "Homens", "D5N": "Mais de 1 a 2 salários mínimos", "V": "5000"},
        ])
        resultado = limpar_renda_por_sm(df)
        assert "Unidade Da Federação" not in resultado["uf"].values
        assert len(resultado) == 1

    def test_remove_pessoas_invalidas(self):
        df = _mock_renda_df([
            {"D1N": "São Paulo", "D4N": "Homens", "D5N": "Mais de 1 a 2 salários mínimos", "V": "-"},
            {"D1N": "São Paulo", "D4N": "Mulheres", "D5N": "Mais de 1 a 2 salários mínimos", "V": "3000"},
        ])
        resultado = limpar_renda_por_sm(df)
        assert len(resultado) == 1
        assert resultado.iloc[0]["pessoas"] == 3000

    def test_bounds_brl_calculados(self):
        """lower_brl e upper_brl devem refletir o SM multiplicado pelo salário mínimo."""
        df = _mock_renda_df([
            {"D1N": "SP", "D4N": "Homens", "D5N": "Mais de 5 a 10 salários mínimos", "V": "100"},
        ])
        resultado = limpar_renda_por_sm(df)
        # 5 SM e 10 SM × R$ 1.212 = R$ 6.060 e R$ 12.120
        from config import SALARIO_MINIMO_CENSO
        assert resultado.iloc[0]["lower_brl"] == pytest.approx(5.0 * SALARIO_MINIMO_CENSO)
        assert resultado.iloc[0]["upper_brl"] == pytest.approx(10.0 * SALARIO_MINIMO_CENSO)

    def test_upper_brl_infinito_para_acima_20_sm(self):
        df = _mock_renda_df([
            {"D1N": "SP", "D4N": "Homens", "D5N": "Mais de 20 salários mínimos", "V": "100"},
        ])
        resultado = limpar_renda_por_sm(df)
        assert resultado.iloc[0]["upper_brl"] == float("inf")


# ─── limpar_estado_conjugal ───────────────────────────────────────────────────

class TestLimparEstadoConjugal:
    def _df_completo(self):
        return _mock_conjugal_df([
            # Faixa válida, sexo válido
            {"D1N": "SP", "D4N": "Não viviam em união", "D5N": "Homens",
             "D6N": "25 a 29 anos", "V": "200"},
            # Faixa inválida → deve ser removida
            {"D1N": "SP", "D4N": "Não viviam em união", "D5N": "Homens",
             "D6N": "18 a 19 anos", "V": "500"},
            # Mulheres, faixa válida
            {"D1N": "SP", "D4N": "Viviam em união", "D5N": "Mulheres",
             "D6N": "30 a 34 anos", "V": "800"},
            # Total UF → deve ser removido
            {"D1N": "Unidade da Federação", "D4N": "Não viviam em união", "D5N": "Homens",
             "D6N": "25 a 29 anos", "V": "9999"},
        ])

    def test_filtra_faixa_etaria_invalida(self):
        resultado = limpar_estado_conjugal(self._df_completo())
        assert "18 a 19 anos" not in resultado["faixa_etaria"].values

    def test_mantem_faixas_validas(self):
        resultado = limpar_estado_conjugal(self._df_completo())
        assert "25 a 29 anos" in resultado["faixa_etaria"].values
        assert "30 a 34 anos" in resultado["faixa_etaria"].values

    def test_remove_linha_total_uf(self):
        resultado = limpar_estado_conjugal(self._df_completo())
        assert "Unidade Da Federação" not in resultado["uf"].values

    def test_colunas_presentes(self):
        resultado = limpar_estado_conjugal(self._df_completo())
        assert set(["uf", "estado_conjugal", "sexo", "faixa_etaria", "pessoas"]).issubset(
            resultado.columns
        )

    def test_pessoas_tipo_int(self):
        resultado = limpar_estado_conjugal(self._df_completo())
        assert resultado["pessoas"].dtype == np.int64

    def test_conta_linhas_corretas(self):
        # Deve sobrar: linha 0 (faixa válida, SP homens) e linha 2 (SP mulheres)
        resultado = limpar_estado_conjugal(self._df_completo())
        assert len(resultado) == 2

"""
Testes para src/analyze.py

Cobrem as funções de análise do funil de realidade:
- calcular_percentual
- _estimar_acima_threshold
- calcular_funil_nacional (com _carregar mockado)
"""
import math
from unittest.mock import patch

import pandas as pd
import pytest

from src.analyze import (
    _estimar_acima_threshold,
    calcular_funil_nacional,
    calcular_percentual,
)
from config import RENDA_MINIMA, SALARIO_MINIMO_CENSO


# ─── calcular_percentual ──────────────────────────────────────────────────────

class TestCalcularPercentual:
    def test_percentual_normal(self):
        assert calcular_percentual(50, 200) == pytest.approx(25.0)

    def test_percentual_cem_por_cento(self):
        assert calcular_percentual(300, 300) == pytest.approx(100.0)

    def test_total_zero_retorna_zero(self):
        assert calcular_percentual(100, 0) == 0.0

    def test_total_none_retorna_zero(self):
        assert calcular_percentual(100, None) == 0.0

    def test_parte_zero_retorna_zero(self):
        assert calcular_percentual(0, 500) == pytest.approx(0.0)

    def test_arredondamento_duas_casas(self):
        # 1/3 * 100 = 33.333... → deve ser 33.33
        resultado = calcular_percentual(1, 3)
        assert resultado == pytest.approx(33.33)


# ─── _estimar_acima_threshold ─────────────────────────────────────────────────

class TestEstimarAcimaThreshold:
    """
    RENDA_MINIMA = R$ 10.000
    SALARIO_MINIMO_CENSO = R$ 1.212
    Brackets SM:
      "5-10 SM" → lower=6060, upper=12120   (straddling)
      "10-15 SM" → lower=12120, upper=18180 (above)
      "1-2 SM"  → lower=1212, upper=2424    (below)
    """

    def _df(self, rows: list[dict]) -> pd.DataFrame:
        return pd.DataFrame(rows)

    def test_todos_abaixo_threshold_retorna_zero(self):
        df = self._df([
            {"lower_brl": 1212.0, "upper_brl": 2424.0, "pessoas": 5000},
            {"lower_brl": 3636.0, "upper_brl": 6060.0, "pessoas": 3000},
        ])
        assert _estimar_acima_threshold(df) == pytest.approx(0.0)

    def test_todos_acima_threshold_retorna_total(self):
        df = self._df([
            {"lower_brl": 12120.0, "upper_brl": 18180.0, "pessoas": 1000},
            {"lower_brl": 18180.0, "upper_brl": 24240.0, "pessoas": 500},
        ])
        assert _estimar_acima_threshold(df) == pytest.approx(1500.0)

    def test_bracket_acima_20sm_com_upper_infinito(self):
        """Brackets "Mais de 20 SM" têm upper=inf e devem ser incluídos inteiros."""
        df = self._df([
            {"lower_brl": 24240.0, "upper_brl": float("inf"), "pessoas": 200},
        ])
        assert _estimar_acima_threshold(df) == pytest.approx(200.0)

    def test_interpolacao_linear_no_bracket_que_cruza_threshold(self):
        """
        Bracket com lower=5000 e upper=15000 (simple numbers for easy math):
        frac = (15000 - 10000) / (15000 - 5000) = 0.5
        Resultado esperado: 0.5 * 1000 = 500
        """
        df = self._df([
            {"lower_brl": 5000.0, "upper_brl": 15000.0, "pessoas": 1000},
        ])
        assert _estimar_acima_threshold(df) == pytest.approx(500.0)

    def test_combinacao_bracket_straddling_e_acima(self):
        """
        Straddling: lower=5000, upper=15000, 1000 pessoas → 500
        Acima:      lower=15000, upper=25000, 300 pessoas → 300
        Total esperado: 800
        """
        df = self._df([
            {"lower_brl": 1000.0,  "upper_brl": 5000.0,  "pessoas": 2000},  # abaixo
            {"lower_brl": 5000.0,  "upper_brl": 15000.0, "pessoas": 1000},  # straddling
            {"lower_brl": 15000.0, "upper_brl": 25000.0, "pessoas": 300},   # acima
        ])
        assert _estimar_acima_threshold(df) == pytest.approx(800.0)

    def test_dataframe_vazio_retorna_zero(self):
        df = self._df([])
        assert _estimar_acima_threshold(df) == pytest.approx(0.0)

    def test_upper_brl_zero_ignorado(self):
        """Bracket com upper_brl=0.0 deve ser ignorado (segurança)."""
        df = self._df([
            {"lower_brl": 0.0, "upper_brl": 0.0, "pessoas": 9999},
            {"lower_brl": 12120.0, "upper_brl": 18180.0, "pessoas": 500},
        ])
        assert _estimar_acima_threshold(df) == pytest.approx(500.0)


# ─── calcular_funil_nacional ──────────────────────────────────────────────────

def _mock_renda() -> pd.DataFrame:
    """
    DataFrame processado de renda com dois brackets para Homens:
    - 5-10 SM (straddling): 1000 pessoas → frac = (12120-10000)/(12120-6060) = 2120/6060
    - 10-15 SM (acima):     500 pessoas  → total incluído
    Total homens empregados = 1500
    """
    sm = SALARIO_MINIMO_CENSO
    return pd.DataFrame([
        {"uf": "São Paulo", "sexo": "Homens",   "classe_sm": "Mais de 5 a 10 salários mínimos",
         "pessoas": 1000, "lower_brl": 5.0 * sm, "upper_brl": 10.0 * sm},
        {"uf": "São Paulo", "sexo": "Homens",   "classe_sm": "Mais de 10 a 15 salários mínimos",
         "pessoas": 500,  "lower_brl": 10.0 * sm, "upper_brl": 15.0 * sm},
        {"uf": "São Paulo", "sexo": "Mulheres", "classe_sm": "Mais de 1 a 2 salários mínimos",
         "pessoas": 8000, "lower_brl": 1.0 * sm,  "upper_brl": 2.0 * sm},
    ])


def _mock_conjugal() -> pd.DataFrame:
    """
    DataFrame de estado conjugal para Homens e Mulheres na faixa 25-44.
    Homens: 200 solteiros, 800 em união → taxa_solt = 0.2
    Mulheres solteiras: 3000
    """
    return pd.DataFrame([
        {"uf": "São Paulo", "sexo": "Homens",   "estado_conjugal": "Não viviam em união",
         "faixa_etaria": "25 a 29 anos", "pessoas": 200},
        {"uf": "São Paulo", "sexo": "Homens",   "estado_conjugal": "Viviam em união",
         "faixa_etaria": "25 a 29 anos", "pessoas": 800},
        {"uf": "São Paulo", "sexo": "Mulheres", "estado_conjugal": "Não viviam em união",
         "faixa_etaria": "25 a 29 anos", "pessoas": 3000},
        {"uf": "São Paulo", "sexo": "Mulheres", "estado_conjugal": "Viviam em união",
         "faixa_etaria": "25 a 29 anos", "pessoas": 2000},
    ])


class TestCalcularFunilNacional:
    @pytest.fixture(autouse=True)
    def _patch_carregar(self):
        with patch("src.analyze._carregar", return_value=(_mock_renda(), _mock_conjugal())):
            yield

    def test_retorna_dicionario(self):
        resultado = calcular_funil_nacional()
        assert isinstance(resultado, dict)

    def test_chaves_presentes(self):
        resultado = calcular_funil_nacional()
        chaves = {"homens_empregados", "homens_10k", "pct_homens_10k",
                  "taxa_solteiros", "homens_10k_solteiros", "mulheres_solteiras", "razao"}
        assert chaves.issubset(resultado.keys())

    def test_homens_empregados(self):
        resultado = calcular_funil_nacional()
        # Homens: 1000 + 500 = 1500
        assert resultado["homens_empregados"] == 1500

    def test_mulheres_solteiras(self):
        resultado = calcular_funil_nacional()
        assert resultado["mulheres_solteiras"] == 3000

    def test_taxa_solteiros(self):
        resultado = calcular_funil_nacional()
        # 200 / (200 + 800) = 0.2
        assert resultado["taxa_solteiros"] == pytest.approx(0.2)

    def test_razao_positiva(self):
        resultado = calcular_funil_nacional()
        assert resultado["razao"] is not None
        assert resultado["razao"] > 0

    def test_pct_homens_10k_menor_que_100(self):
        resultado = calcular_funil_nacional()
        assert 0.0 < resultado["pct_homens_10k"] < 100.0

    def test_razao_com_zero_homens_retorna_none(self):
        renda_vazia = pd.DataFrame([
            {"uf": "SP", "sexo": "Homens", "classe_sm": "Até 1/4 de salário mínimo",
             "pessoas": 0, "lower_brl": 0.0, "upper_brl": 303.0},
        ])
        with patch("src.analyze._carregar", return_value=(renda_vazia, _mock_conjugal())):
            resultado = calcular_funil_nacional()
        assert resultado["razao"] is None

    def test_ano_referencia(self):
        resultado = calcular_funil_nacional()
        assert resultado["ano_referencia"] == 2022

    def test_renda_minima(self):
        resultado = calcular_funil_nacional()
        assert resultado["renda_minima"] == RENDA_MINIMA

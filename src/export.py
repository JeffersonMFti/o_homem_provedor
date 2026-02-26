import json
import pandas as pd

from config import DATA_PROCESSED, WEB_DATA, SEXO_MASCULINO, RENDA_MINIMA


def _salvar_json(dados, nome: str) -> None:
    WEB_DATA.mkdir(parents=True, exist_ok=True)
    with open(WEB_DATA / f"{nome}.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


def exportar_funil_nacional(funil: dict) -> None:
    _salvar_json(funil, "funil_nacional")


def exportar_funil_por_estado(df: pd.DataFrame) -> None:
    records = df.to_dict(orient="records")
    _salvar_json(records, "funil_por_estado")


def exportar_distribuicao_renda(df_renda: pd.DataFrame) -> None:
    """Distribuição nacional de homens empregados por faixa de renda em SM."""
    nacional = (
        df_renda[df_renda["sexo"] == SEXO_MASCULINO]
        .groupby("classe_sm", sort=False)
        .agg(pessoas=("pessoas", "sum"), lower_brl=("lower_brl", "first"), upper_brl=("upper_brl", "first"))
        .reset_index()
        .sort_values("lower_brl")
    )

    total = nacional["pessoas"].sum()
    nacional["pct"] = (nacional["pessoas"] / total * 100).round(2)
    nacional["acima_threshold"] = nacional["lower_brl"] >= RENDA_MINIMA

    registros = nacional[["classe_sm", "pessoas", "pct", "lower_brl", "upper_brl", "acima_threshold"]].to_dict(
        orient="records"
    )
    _salvar_json(registros, "distribuicao_renda")


def exportar_razao_por_uf(df: pd.DataFrame) -> None:
    """Razão mulheres solteiras / homens solteiros 10k+ por UF — para o mapa."""
    registros = (
        df[["uf", "razao", "homens_10k_solteiros", "mulheres_solteiras", "pct_homens_10k"]]
        .to_dict(orient="records")
    )
    _salvar_json(registros, "razao_por_uf")

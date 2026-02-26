import sidrapy
import pandas as pd
from pathlib import Path

from config import (
    DATA_RAW,
    CENSO_RENDA_SM,
    CENSO_CONJUGAL,
    CENSO_OCUPADOS_FAIXA,
)

# Grupo de idade codes (25-44 anos no SIDRA)
_IDADE_25_44 = "1145,1146,1147,1148"

# Estado conjugal codes: Total (50292), Viviam em união (12108), Não viviam (12109)
_CONJUGAL_TODOS = "allxt"

# SM income classes: all except total
_SM_CLASSES = "allxt"


def _salvar_raw(df: pd.DataFrame, nome: str) -> None:
    DATA_RAW.mkdir(parents=True, exist_ok=True)
    df.to_csv(DATA_RAW / f"{nome}.csv", index=False, encoding="utf-8")


def buscar_renda_por_sm(forcar: bool = False) -> pd.DataFrame:
    destino = DATA_RAW / "renda_por_sm.csv"
    if destino.exists() and not forcar:
        return pd.read_csv(destino)

    df = sidrapy.get_table(
        table_code=CENSO_RENDA_SM,
        territorial_level="3",
        ibge_territorial_code="all",
        variable="4090",
        classifications={"2": "4,5", "11915": _SM_CLASSES},
        period="last 1",
        header="y",
        format="pandas",
    )
    _salvar_raw(df, "renda_por_sm")
    return df


def buscar_estado_conjugal(forcar: bool = False) -> pd.DataFrame:
    destino = DATA_RAW / "estado_conjugal.csv"
    if destino.exists() and not forcar:
        return pd.read_csv(destino)

    df = sidrapy.get_table(
        table_code=CENSO_CONJUGAL,
        territorial_level="3",
        ibge_territorial_code="all",
        variable="140",
        classifications={"464": _CONJUGAL_TODOS, "2": "4,5", "58": _IDADE_25_44, "86": "95251"},
        period="last 1",
        header="y",
        format="pandas",
    )
    _salvar_raw(df, "estado_conjugal")
    return df


def buscar_ocupados_por_faixa(forcar: bool = False) -> pd.DataFrame:
    destino = DATA_RAW / "ocupados_por_faixa.csv"
    if destino.exists() and not forcar:
        return pd.read_csv(destino)

    df = sidrapy.get_table(
        table_code=CENSO_OCUPADOS_FAIXA,
        territorial_level="3",
        ibge_territorial_code="all",
        variable="140",
        classifications={"2": "4,5", "86": "95251", "58": _IDADE_25_44},
        period="last 1",
        header="y",
        format="pandas",
    )
    _salvar_raw(df, "ocupados_por_faixa")
    return df

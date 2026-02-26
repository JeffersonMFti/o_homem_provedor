import pandas as pd
import numpy as np

from config import (
    DATA_RAW,
    DATA_PROCESSED,
    FAIXA_ETARIA,
    SEXO_MASCULINO,
    SEXO_FEMININO,
    ESTADO_CONJUGAL_SEM_UNIAO,
    SALARIO_MINIMO_CENSO,
    RENDA_MINIMA,
)

# SM classes → (lower_bound_sm, upper_bound_sm)
_SM_BOUNDS: dict[str, tuple[float, float]] = {
    "Até 1/4 de salário mínimo":           (0.0,   0.25),
    "Mais de 1/4 a 1/2 salário mínimo":    (0.25,  0.5),
    "Mais de 1/2 a 1 salário mínimo":      (0.5,   1.0),
    "Mais de 1 a 2 salários mínimos":      (1.0,   2.0),
    "Mais de 2 a 3 salários mínimos":      (2.0,   3.0),
    "Mais de 3 a 5 salários mínimos":      (3.0,   5.0),
    "Mais de 5 a 10 salários mínimos":     (5.0,  10.0),
    "Mais de 10 a 15 salários mínimos":   (10.0,  15.0),
    "Mais de 15 a 20 salários mínimos":   (15.0,  20.0),
    "Mais de 20 salários mínimos":        (20.0, float("inf")),
    "Sem rendimento":                      (0.0,   0.0),
}


def _drop_header_row(df: pd.DataFrame) -> pd.DataFrame:
    return df.iloc[1:].copy().reset_index(drop=True)


def _to_int(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series.replace(["-", "...", "X"], np.nan), errors="coerce")


def _normalizar_uf(series: pd.Series) -> pd.Series:
    return series.str.strip().str.title()


def _salvar_processed(df: pd.DataFrame, nome: str) -> None:
    DATA_PROCESSED.mkdir(parents=True, exist_ok=True)
    df.to_csv(DATA_PROCESSED / f"{nome}.csv", index=False, encoding="utf-8")


def limpar_renda_por_sm(df: pd.DataFrame) -> pd.DataFrame:
    df = _drop_header_row(df)

    df = df.rename(columns={
        "D1N": "uf",
        "D4N": "sexo",
        "D5N": "classe_sm",
        "V":   "pessoas",
    })[["uf", "sexo", "classe_sm", "pessoas"]]

    # Remove a linha de total da UF (primeira linha com label genérico)
    df = df[~df["uf"].isin(["Unidade da Federação"])].copy()

    df["pessoas"] = _to_int(df["pessoas"])
    df = df.dropna(subset=["pessoas"])
    df["pessoas"] = df["pessoas"].astype(int)

    df["uf"] = _normalizar_uf(df["uf"])

    # Remove "Sem rendimento" — não contribui para o funil de renda
    df = df[df["classe_sm"] != "Sem rendimento"].copy()

    # Converte bounds de SM para R$
    df["lower_brl"] = df["classe_sm"].map(
        lambda c: _SM_BOUNDS.get(c, (np.nan, np.nan))[0] * SALARIO_MINIMO_CENSO
    )
    df["upper_brl"] = df["classe_sm"].map(
        lambda c: _SM_BOUNDS.get(c, (np.nan, np.nan))[1] * SALARIO_MINIMO_CENSO
    )

    return df.reset_index(drop=True)


def limpar_estado_conjugal(df: pd.DataFrame) -> pd.DataFrame:
    df = _drop_header_row(df)

    df = df.rename(columns={
        "D1N": "uf",
        "D4N": "estado_conjugal",
        "D5N": "sexo",
        "D6N": "faixa_etaria",
        "V":   "pessoas",
    })[["uf", "estado_conjugal", "sexo", "faixa_etaria", "pessoas"]]

    df = df[~df["uf"].isin(["Unidade da Federação"])].copy()
    df = df[df["faixa_etaria"].isin(FAIXA_ETARIA)].copy()
    df = df[df["sexo"].isin([SEXO_MASCULINO, SEXO_FEMININO])].copy()

    df["pessoas"] = _to_int(df["pessoas"])
    df = df.dropna(subset=["pessoas"])
    df["pessoas"] = df["pessoas"].astype(int)

    df["uf"] = _normalizar_uf(df["uf"])

    return df.reset_index(drop=True)


def limpar_ocupados_por_faixa(df: pd.DataFrame) -> pd.DataFrame:
    df = _drop_header_row(df)

    df = df.rename(columns={
        "D1N": "uf",
        "D4N": "sexo",
        "D6N": "faixa_etaria",
        "V":   "pessoas",
    })[["uf", "sexo", "faixa_etaria", "pessoas"]]

    df = df[~df["uf"].isin(["Unidade da Federação"])].copy()
    df = df[df["faixa_etaria"].isin(FAIXA_ETARIA)].copy()
    df = df[df["sexo"].isin([SEXO_MASCULINO, SEXO_FEMININO])].copy()

    df["pessoas"] = _to_int(df["pessoas"])
    df = df.dropna(subset=["pessoas"])
    df["pessoas"] = df["pessoas"].astype(int)

    df["uf"] = _normalizar_uf(df["uf"])

    return df.reset_index(drop=True)


def processar_tudo() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    renda = limpar_renda_por_sm(
        pd.read_csv(DATA_RAW / "renda_por_sm.csv", encoding="utf-8")
    )
    conjugal = limpar_estado_conjugal(
        pd.read_csv(DATA_RAW / "estado_conjugal.csv", encoding="utf-8")
    )
    ocupados = limpar_ocupados_por_faixa(
        pd.read_csv(DATA_RAW / "ocupados_por_faixa.csv", encoding="utf-8")
    )

    _salvar_processed(renda, "renda_por_sm")
    _salvar_processed(conjugal, "estado_conjugal")
    _salvar_processed(ocupados, "ocupados_por_faixa")

    return renda, conjugal, ocupados

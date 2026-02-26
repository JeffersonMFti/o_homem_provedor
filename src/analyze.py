import pandas as pd
import numpy as np

from config import (
    DATA_PROCESSED,
    RENDA_MINIMA,
    SEXO_MASCULINO,
    SEXO_FEMININO,
    ESTADO_CONJUGAL_SEM_UNIAO,
    ANO_REFERENCIA,
)


def calcular_percentual(parte: int | float, total: int | float) -> float:
    if not total or total == 0:
        return 0.0
    return round((parte / total) * 100, 2)


def _estimar_acima_threshold(df: pd.DataFrame) -> float:
    """
    Soma as pessoas com rendimento >= RENDA_MINIMA, interpolando linearmente
    dentro do bracket que contém o threshold.
    """
    total = 0.0
    for _, row in df.iterrows():
        lower, upper = row["lower_brl"], row["upper_brl"]
        if upper == 0.0:  # "Sem rendimento" já removido, mas por segurança
            continue
        if lower >= RENDA_MINIMA:
            total += row["pessoas"]
        elif upper > RENDA_MINIMA and lower < RENDA_MINIMA:
            if upper == float("inf"):
                total += row["pessoas"]
            else:
                frac = (upper - RENDA_MINIMA) / (upper - lower)
                total += row["pessoas"] * frac
    return total


def _carregar() -> tuple[pd.DataFrame, pd.DataFrame]:
    renda = pd.read_csv(DATA_PROCESSED / "renda_por_sm.csv", encoding="utf-8")
    conjugal = pd.read_csv(DATA_PROCESSED / "estado_conjugal.csv", encoding="utf-8")
    return renda, conjugal


def _taxa_solteiros(df_conjugal_uf_sexo: pd.DataFrame) -> float:
    sem_uniao = df_conjugal_uf_sexo[
        df_conjugal_uf_sexo["estado_conjugal"] == ESTADO_CONJUGAL_SEM_UNIAO
    ]["pessoas"].sum()
    total = df_conjugal_uf_sexo["pessoas"].sum()
    return sem_uniao / total if total else 0.0


def calcular_funil_nacional() -> dict:
    renda, conjugal = _carregar()

    # Homens com renda >= R$10k (todos os empregados, todas as idades)
    homens_renda = renda[renda["sexo"] == SEXO_MASCULINO]
    homens_10k = _estimar_acima_threshold(homens_renda)

    # Total de homens empregados (denominador para % nacional)
    homens_empregados = homens_renda["pessoas"].sum()
    pct_10k = calcular_percentual(homens_10k, homens_empregados)

    # Taxa de solteiros (não viviam em união) entre homens 25-44
    conj_h = conjugal[conjugal["sexo"] == SEXO_MASCULINO]
    taxa_solt = _taxa_solteiros(conj_h)

    # Proxy: assume que a taxa de solteiros do grupo 25-44 se aplica aos
    # homens de alta renda. Documentado como limitação metodológica.
    homens_10k_solteiros = round(homens_10k * taxa_solt)

    # Mulheres solteiras 25-44
    mulheres_solteiras = int(
        conjugal[
            (conjugal["sexo"] == SEXO_FEMININO) &
            (conjugal["estado_conjugal"] == ESTADO_CONJUGAL_SEM_UNIAO)
        ]["pessoas"].sum()
    )

    razao = (
        round(mulheres_solteiras / homens_10k_solteiros, 1)
        if homens_10k_solteiros else None
    )

    return {
        "ano_referencia": ANO_REFERENCIA,
        "renda_minima": RENDA_MINIMA,
        "homens_empregados": int(homens_empregados),
        "homens_10k": round(homens_10k),
        "pct_homens_10k": pct_10k,
        "taxa_solteiros": round(taxa_solt, 4),
        "homens_10k_solteiros": homens_10k_solteiros,
        "mulheres_solteiras": mulheres_solteiras,
        "razao": razao,
    }


def calcular_funil_por_uf() -> pd.DataFrame:
    renda, conjugal = _carregar()

    ufs = sorted(renda["uf"].unique())
    rows = []

    for uf in ufs:
        r_h = renda[(renda["uf"] == uf) & (renda["sexo"] == SEXO_MASCULINO)]
        homens_10k = _estimar_acima_threshold(r_h)
        homens_emp = r_h["pessoas"].sum()
        pct_10k = calcular_percentual(homens_10k, homens_emp)

        c_uf = conjugal[conjugal["uf"] == uf]
        taxa_solt = _taxa_solteiros(c_uf[c_uf["sexo"] == SEXO_MASCULINO])
        homens_10k_solt = round(homens_10k * taxa_solt)

        mulheres_solt = int(
            c_uf[
                (c_uf["sexo"] == SEXO_FEMININO) &
                (c_uf["estado_conjugal"] == ESTADO_CONJUGAL_SEM_UNIAO)
            ]["pessoas"].sum()
        )

        razao = round(mulheres_solt / homens_10k_solt, 1) if homens_10k_solt else None

        rows.append({
            "uf": uf,
            "homens_10k": round(homens_10k),
            "pct_homens_10k": pct_10k,
            "taxa_solteiros": round(taxa_solt, 4),
            "homens_10k_solteiros": homens_10k_solt,
            "mulheres_solteiras": mulheres_solt,
            "razao": razao,
        })

    return (
        pd.DataFrame(rows)
        .sort_values("razao", ascending=False)
        .reset_index(drop=True)
    )

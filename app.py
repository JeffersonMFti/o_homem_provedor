import sys
sys.path.insert(0, ".")

import streamlit as st
import pandas as pd
import json

from src.analyze import calcular_funil_nacional, calcular_funil_por_uf
from src.visualize import (
    grafico_distribuicao_renda,
    grafico_funil,
    grafico_barras_uf,
)
from config import DATA_PROCESSED

st.set_page_config(
    page_title="R$ 10k ou nada? — Analise",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("R$ 10k ou nada?")
st.markdown("Analise de dados do Censo Demografico 2022 — IBGE")

with st.spinner("Calculando..."):
    funil = calcular_funil_nacional()
    df_uf = calcular_funil_por_uf()
    renda = pd.read_csv(DATA_PROCESSED / "renda_por_sm.csv", encoding="utf-8")

    with open("web/data/distribuicao_renda.json", encoding="utf-8") as f:
        dist_renda = pd.DataFrame(json.load(f))

col1, col2, col3 = st.columns(3)
col1.metric("Homens empregados", f"{funil['homens_empregados']:,}")
col2.metric("Ganham R$ 10k+", f"{funil['homens_10k']:,}", f"{funil['pct_homens_10k']:.1f}%")
col3.metric("Razao nacional", f"{funil['razao']}x")

st.markdown("---")

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Distribuicao de renda")
    st.plotly_chart(grafico_distribuicao_renda(dist_renda), use_container_width=True)

with col_b:
    st.subheader("O funil")
    st.plotly_chart(grafico_funil(funil), use_container_width=True)

st.markdown("---")
st.subheader("Razao por estado")
st.plotly_chart(grafico_barras_uf(df_uf), use_container_width=True)

st.markdown("---")
st.subheader("Dados por estado")
st.dataframe(
    df_uf.rename(columns={
        "uf": "Estado",
        "homens_10k": "Homens R$10k+",
        "pct_homens_10k": "% dos empregados",
        "taxa_solteiros": "Taxa solteiros",
        "homens_10k_solteiros": "Homens solteiros R$10k+",
        "mulheres_solteiras": "Mulheres solteiras",
        "razao": "Razao",
    }),
    use_container_width=True,
)

st.caption(
    "Fonte: Censo Demografico 2022, IBGE. "
    "Metodologia: interpolacao linear dentro do bracket de 5-10 SM para estimar homens com renda >= R$10k. "
    "Taxa de solteiros do grupo 25-44 aplicada como proxy ao grupo de alta renda."
)

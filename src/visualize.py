import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

_CORES = {
    "primaria": "#1a1a2e",
    "destaque": "#e94560",
    "suave": "#16213e",
    "texto": "#eaeaea",
    "barra_base": "#2d4059",
    "barra_10k": "#e94560",
}

_LAYOUT_BASE = {
    "plot_bgcolor": "rgba(0,0,0,0)",
    "paper_bgcolor": "rgba(0,0,0,0)",
    "font": {"color": _CORES["texto"], "family": "Inter, sans-serif"},
    "margin": {"t": 40, "b": 40, "l": 60, "r": 20},
}


def grafico_distribuicao_renda(df: pd.DataFrame) -> go.Figure:
    """Histograma de homens empregados por faixa de renda em SM."""
    cores = [
        _CORES["barra_10k"] if row["acima_threshold"] else _CORES["barra_base"]
        for _, row in df.iterrows()
    ]

    fig = go.Figure(
        go.Bar(
            x=df["classe_sm"],
            y=df["pct"],
            marker_color=cores,
            text=df["pct"].apply(lambda v: f"{v:.1f}%"),
            textposition="outside",
            hovertemplate="%{x}<br>%{y:.1f}% dos homens empregados<extra></extra>",
        )
    )

    fig.update_layout(
        **_LAYOUT_BASE,
        title="Distribuicao de homens empregados por faixa de renda",
        xaxis={"title": "", "tickangle": -30},
        yaxis={"title": "% dos homens empregados", "showgrid": True, "gridcolor": "#333"},
    )
    return fig


def grafico_funil(funil: dict) -> go.Figure:
    """Funil de realidade: do total de homens ao pool de alta renda e solteiros."""
    etapas = [
        ("Homens empregados", funil["homens_empregados"]),
        ("Ganham R$ 10k+", funil["homens_10k"]),
        ("Solteiros R$ 10k+", funil["homens_10k_solteiros"]),
    ]
    labels = [e[0] for e in etapas]
    valores = [e[1] for e in etapas]

    fig = go.Figure(
        go.Funnel(
            y=labels,
            x=valores,
            textinfo="value+percent initial",
            marker_color=[_CORES["suave"], _CORES["barra_base"], _CORES["barra_10k"]],
            connector={"line": {"color": "#444", "width": 1}},
        )
    )

    fig.update_layout(
        **_LAYOUT_BASE,
        title="O funil da realidade",
    )
    return fig


def grafico_mapa_razao(df: pd.DataFrame) -> go.Figure:
    """Mapa coroplético com a razão mulheres solteiras / homens solteiros 10k+ por UF."""
    fig = px.choropleth(
        df,
        geojson="https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson",
        locations="uf",
        featureidkey="properties.name",
        color="razao",
        color_continuous_scale="RdYlGn_r",
        hover_data={"razao": True, "homens_10k_solteiros": True, "mulheres_solteiras": True},
        labels={"razao": "Razao"},
    )
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
        **_LAYOUT_BASE,
        title="Razao por estado",
        coloraxis_colorbar={"title": "Razao"},
    )
    return fig


def grafico_barras_uf(df: pd.DataFrame) -> go.Figure:
    """Ranking horizontal de UFs por razão."""
    df_ord = df.sort_values("razao")
    cores = [
        _CORES["barra_10k"] if r >= df["razao"].median() else _CORES["barra_base"]
        for r in df_ord["razao"]
    ]

    fig = go.Figure(
        go.Bar(
            x=df_ord["razao"],
            y=df_ord["uf"],
            orientation="h",
            marker_color=cores,
            text=df_ord["razao"].apply(lambda v: f"{v:.1f}x"),
            textposition="outside",
            hovertemplate="%{y}<br>Razao: %{x:.1f}<extra></extra>",
        )
    )

    fig.update_layout(
        **_LAYOUT_BASE,
        title="Razao por estado (ranking)",
        xaxis={"title": "Mulheres solteiras por homem solteiro com renda 10k+"},
        yaxis={"title": ""},
        height=700,
    )
    return fig

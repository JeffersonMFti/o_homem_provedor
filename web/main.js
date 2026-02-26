'use strict';

const COR_BASE    = '#2d4059';
const COR_10K     = '#e94560';
const COR_TEXTO   = '#e0e0e0';
const COR_GRADE   = '#2a2a40';
const BG_TRANS    = 'rgba(0,0,0,0)';

const layoutBase = {
  paper_bgcolor: BG_TRANS,
  plot_bgcolor:  BG_TRANS,
  font: { color: COR_TEXTO, family: 'Segoe UI, Inter, system-ui, sans-serif', size: 13 },
  margin: { t: 40, b: 60, l: 60, r: 20 },
};

function fmt(n) {
  return n == null ? '—' : Number(n).toLocaleString('pt-BR');
}

function renderDistribuicao(dados) {
  const cores = dados.map(d => d.acima_threshold ? COR_10K : COR_BASE);

  const trace = {
    type: 'bar',
    x: dados.map(d => d.classe_sm),
    y: dados.map(d => d.pct),
    marker: { color: cores },
    text: dados.map(d => d.pct.toFixed(1) + '%'),
    textposition: 'outside',
    hovertemplate: '%{x}<br>%{y:.1f}% dos homens empregados<extra></extra>',
  };

  const layout = {
    ...layoutBase,
    xaxis: { tickangle: -30, color: COR_TEXTO, gridcolor: COR_GRADE },
    yaxis: { title: '% dos homens empregados', color: COR_TEXTO, gridcolor: COR_GRADE },
  };

  Plotly.newPlot('chart-distribuicao', [trace], layout, { responsive: true });
}

function renderFunil(funil) {
  const trace = {
    type: 'funnel',
    y: ['Homens empregados', 'Ganham R$ 10k+', 'Solteiros R$ 10k+'],
    x: [funil.homens_empregados, funil.homens_10k, funil.homens_10k_solteiros],
    textinfo: 'value+percent initial',
    marker: { color: ['#16213e', COR_BASE, COR_10K] },
    connector: { line: { color: '#444', width: 1 } },
  };

  Plotly.newPlot('chart-funil', [trace], { ...layoutBase }, { responsive: true });
}

function renderMapa(dados) {
  const ufs     = dados.map(d => d.uf);
  const razoes  = dados.map(d => d.razao);

  const trace = {
    type: 'choropleth',
    geojson: 'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson',
    locations: ufs,
    featureidkey: 'properties.name',
    z: razoes,
    colorscale: 'RdYlGn',
    reversescale: true,
    colorbar: { title: 'Razão', tickfont: { color: COR_TEXTO }, titlefont: { color: COR_TEXTO } },
    hovertemplate: '%{location}<br>Razão: %{z:.1f}<extra></extra>',
  };

  const layout = {
    ...layoutBase,
    geo: {
      fitbounds: 'locations',
      visible: false,
      bgcolor: BG_TRANS,
    },
  };

  Plotly.newPlot('chart-mapa', [trace], layout, { responsive: true });
}

function renderBarras(dados) {
  const ordenado = [...dados].sort((a, b) => a.razao - b.razao);
  const mediana  = dados.map(d => d.razao).sort((a, b) => a - b)[Math.floor(dados.length / 2)];
  const cores    = ordenado.map(d => d.razao >= mediana ? COR_10K : COR_BASE);

  const trace = {
    type: 'bar',
    orientation: 'h',
    x: ordenado.map(d => d.razao),
    y: ordenado.map(d => d.uf),
    marker: { color: cores },
    text: ordenado.map(d => d.razao.toFixed(1) + 'x'),
    textposition: 'outside',
    hovertemplate: '%{y}<br>Razão: %{x:.1f}<extra></extra>',
  };

  const layout = {
    ...layoutBase,
    height: 700,
    margin: { ...layoutBase.margin, l: 140 },
    xaxis: { title: 'Mulheres solteiras por homem solteiro R$10k+', color: COR_TEXTO, gridcolor: COR_GRADE },
    yaxis: { color: COR_TEXTO },
  };

  Plotly.newPlot('chart-barras', [trace], layout, { responsive: true });
}

function preencherMetricas(funil) {
  const razao = funil.razao != null ? funil.razao.toFixed(1) + 'x' : '—';

  document.getElementById('razao-nacional').textContent = razao;
  document.getElementById('razao-nacional-2').textContent = razao;
  document.getElementById('pct-10k').textContent = funil.pct_homens_10k.toFixed(1) + '%';
  document.getElementById('homens-solteiros').textContent = fmt(funil.homens_10k_solteiros);
  document.getElementById('mulheres-solteiras').textContent = fmt(funil.mulheres_solteiras);
}

async function init() {
  try {
    const [funil, estados, distribuicao, razaoUf] = await Promise.all([
      fetch('./data/funil_nacional.json').then(r => { if (!r.ok) throw new Error(r.status); return r.json(); }),
      fetch('./data/funil_por_estado.json').then(r => { if (!r.ok) throw new Error(r.status); return r.json(); }),
      fetch('./data/distribuicao_renda.json').then(r => { if (!r.ok) throw new Error(r.status); return r.json(); }),
      fetch('./data/razao_por_uf.json').then(r => { if (!r.ok) throw new Error(r.status); return r.json(); }),
    ]);

    preencherMetricas(funil);
    renderDistribuicao(distribuicao);
    renderFunil(funil);
    renderMapa(razaoUf);
    renderBarras(estados);
  } catch (err) {
    console.error('Erro ao carregar dados:', err);
  }
}

document.addEventListener('DOMContentLoaded', init);

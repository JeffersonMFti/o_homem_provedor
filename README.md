# R$ 10k ou nada?: Uma análise do mercado de trabalho brasileiro

> *"Pra namorar comigo, ele precisa ganhar pelo menos 10 mil por mês."*  
> A frase que tomou as redes. A matemática que ninguém foi atrás.

---

## O que é isso

Este projeto é uma análise de dados baseada em fontes públicas do IBGE que tenta responder, com seriedade e um toque de ironia, uma pergunta que viralizou nas redes sociais: **o quanto esse homem de R$ 10k é realmente comum no Brasil?**

Não é uma crítica. É uma análise. Os dados falam por si.

🌐 **[Acesse a visualização pública do projeto →](https://o-homem-provedor.vercel.app)**

---

## Por que fiz isso

Redes sociais têm a habilidade de transformar exceção em regra. Um padrão que existe em bolsões específicos do país, grandes capitais, setores específicos, faixas etárias privilegiadas, começa a parecer o mínimo esperável. Este projeto existe pra colocar esse número em perspectiva real, com dados do mercado formal de trabalho brasileiro.

---

## O que você vai encontrar aqui

A análise foi construída como um funil de realidade em três etapas:

**1. A renda**  
Qual o percentual de homens economicamente ativos que de fato recebe R$ 10.000 ou mais por mês? Distribuição por estado, escolaridade e setor.

**2. A disponibilidade**  
Desse grupo, quantos estão solteiros? O pool de candidatos afunila consideravelmente quando o estado civil entra na equação.

**3. A proporção**  
Para completar o quadro: quantas mulheres solteiras existem na mesma faixa etária? A razão final entre oferta e demanda é onde a matemática fica mais interessante.

---

## Estrutura do repositório

```
o_homem_provedor/
├── data/
│   ├── raw/              # Dados brutos extraídos da API do IBGE
│   └── processed/        # Dados tratados prontos para análise
├── notebooks/            # Exploração e validação das análises
├── src/
│   ├── collect.py        # Coleta via sidrapy
│   ├── process.py        # Limpeza e transformação
│   ├── analyze.py        # Cálculos e métricas do funil
│   ├── visualize.py      # Geração dos gráficos (Plotly Python)
│   └── export.py         # Exportação dos resultados para JSON
├── web/                  # Site público hospedado no Vercel
│   ├── index.html
├── web/                  # Site público hospedado no Vercel
│   ├── index.html
│   ├── style.css
│   └── main.js           # Consome os JSONs e renderiza via Plotly.js
├── app.py                # Dashboard local em Streamlit
├── gerar_relatorio_pdf.py # Gera relatório completo em PDF
├── run_pipeline.py       # Executa o pipeline completo e exporta os JSONs
├── serve_web.py          # Servidor HTTP local para visualização web
├── requirements.txt
└── README.md
```

---

## Como rodar localmente

### Opção 1: Visualização Web (recomendado)

```bash
# Clone o repositório
git clone https://github.com/JeffersonMFti/o_homem_provedor.git
cd o_homem_provedor

# Execute o pipeline para gerar os dados (se ainda não existirem)
python run_pipeline.py

# Inicie o servidor web local
python serve_web.py

# Acesse no navegador: http://localhost:8000
```

**Nota importante:** Não abra o arquivo `web/index.html` diretamente no navegador (via `file://`), pois isso causa erros de CORS que impedem o carregamento dos dados. Use sempre o servidor HTTP local.

### Opção 2: Dashboard interativo com Streamlit

```bash
# Clone o repositório
git clone https://github.com/JeffersonMFti/o_homem_provedor.git
cd o_homem_provedor

# Crie o ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Execute o pipeline completo (coleta → processamento → análise → exporta JSONs)
python run_pipeline.py

# Acesse o dashboard local
streamlit run app.py
```

### Opção 3: Relatório em PDF

Para gerar um relatório completo e profissional em PDF com todos os dados e análises:

```bash
# Certifique-se de que os dados foram gerados
python run_pipeline.py

# Gere o relatório PDF
python gerar_relatorio_pdf.py

# O arquivo relatorio_10k_ou_nada.pdf será criado na raiz do projeto
```

**O relatório PDF inclui:**
- Capa com informações do projeto
- Introdução e contexto
- Metodologia detalhada e limitações
- Resultados nacionais com métricas principais
- Distribuição completa de renda por faixas
- Análise comparativa por todos os estados
- Tabelas com dados completos
- Conclusões e implicações
- Anexo técnico com especificações das fontes

**Requisitos:** O relatório utiliza `reportlab` e `kaleido` (já incluídos no `requirements.txt`).

---

## Problemas comuns

### Os dados não aparecem na página web?

**Causa mais comum:** Você está abrindo o arquivo HTML diretamente (URL começa com `file://`).

**Solução rápida:** 
```bash
python serve_web.py
# Acesse: http://localhost:8000
```

Para mais detalhes sobre este e outros problemas, consulte o guia completo: **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)**

---

## Fonte dos dados

Todos os dados utilizados são públicos e disponibilizados pelo IBGE através do **Censo Demográfico 2022**, acessados via API SIDRA (tabelas 10292, 10185 e 10268).

Nenhum dado foi estimado ou fabricado. O que está aqui é o que o Brasil reporta sobre si mesmo.

---

## Stack

**Análise (Python)**
- Pandas / NumPy, processamento e cruzamento das variáveis
- sidrapy, acesso à API do IBGE
- Plotly, visualizações no dashboard local
- Streamlit, dashboard local para exploração

**Site público (Vercel)**
- HTML / CSS / JavaScript
- Plotly.js, renderização dos gráficos no browser
- JSONs estáticos gerados pelo pipeline Python

---

## Resultado

No final da análise, um número simples resume tudo:

> **Para cada homem solteiro que ganha R$ 10k ou mais, existem X mulheres solteiras na mesma faixa etária.**

Esse número varia por estado. Em alguns lugares, o desequilíbrio é bem mais acentuado do que o imaginado.

---

## Observação final

Este projeto não tem a intenção de invalidar expectativas pessoais de ninguém. O objetivo é trazer contexto: quando você entende o tamanho real de um grupo populacional, você passa a enxergar melhor onde está a exceção e onde está a regra.

Dados não julgam. Apenas informam.

---

*Desenvolvido por [Jefferson Monteiro](https://github.com/JeffersonMFti), Análise de dados com Python e fontes públicas brasileiras.*

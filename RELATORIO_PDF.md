# Relatório PDF - Guia de Uso

Este documento explica como gerar e customizar o relatório PDF completo do projeto "R$ 10k ou nada?".

## 📄 Visão Geral

O relatório PDF é um documento profissional que contém todas as análises, dados e conclusões do projeto em formato imprimível e compartilhável. É ideal para:

- Apresentações acadêmicas
- Compartilhamento offline
- Arquivo permanente dos resultados
- Análise detalhada da metodologia

## 🚀 Gerando o Relatório

### Passo 1: Certifique-se de que as dependências estão instaladas

```bash
pip install -r requirements.txt
```

As bibliotecas necessárias são:
- `reportlab` - Geração de PDFs
- `kaleido` - Exportação de gráficos Plotly
- `pandas`, `plotly` - Processamento e visualização

### Passo 2: Gere os dados (se ainda não tiver feito)

```bash
python run_pipeline.py
```

Isso criará os arquivos JSON em `web/data/`:
- `funil_nacional.json`
- `funil_por_estado.json`
- `distribuicao_renda.json`
- `razao_por_uf.json`

### Passo 3: Execute o gerador de relatório

```bash
python gerar_relatorio_pdf.py
```

O processo levará alguns segundos e você verá o progresso:

```
============================================================
Gerador de Relatório PDF - Projeto R$ 10k ou nada?
============================================================

[1/7] Verificando dados...
   ✓ Todos os arquivos de dados encontrados
[2/7] Carregando dados...
   ✓ Dados carregados: 27 estados
[3/7] Criando estrutura do documento...
[4/7] Gerando capa e introdução...
[5/7] Gerando seções de metodologia e resultados...
[6/7] Gerando análise por estados...
[7/7] Finalizando relatório...

Gerando arquivo PDF...

============================================================
✓ Relatório gerado com sucesso: relatorio_10k_ou_nada.pdf
  Tamanho: 64.2 KB
============================================================
```

### Passo 4: Abra o relatório

O arquivo `relatorio_10k_ou_nada.pdf` será criado na raiz do projeto. Você pode abri-lo com qualquer leitor de PDF.

## 📋 Conteúdo do Relatório

O relatório gerado contém aproximadamente 10-15 páginas com as seguintes seções:

### 1. Capa
- Título do projeto
- Frase de efeito
- Subtítulo com contexto
- Informações técnicas (fonte, data, ano de referência)

### 2. Introdução
- Contexto e motivação do projeto
- Três questões fundamentais abordadas
- Objetivo da análise

### 3. Metodologia
- Descrição das 4 etapas do funil de análise
- Tabela com fontes de dados (tabelas SIDRA)
- Limitações metodológicas detalhadas
- Definições e premissas utilizadas

### 4. Resultados Nacionais
- Resumo executivo em destaque
- Tabela de métricas principais:
  - Total de homens empregados
  - Homens que ganham R$ 10k+
  - Homens solteiros com R$ 10k+
  - Mulheres solteiras
  - Razão nacional
- Interpretação dos resultados

### 5. Distribuição de Renda
- Tabela completa com todas as faixas de salário mínimo
- Percentuais de homens em cada faixa
- Destaque visual para faixas acima de R$ 10k
- Gráfico de distribuição (se disponível)

### 6. Análise por Estado
- Top 5 estados com menor razão (melhores para a demanda)
- Top 5 estados com maior razão (piores para a demanda)
- Tabelas coloridas para fácil visualização
- Comparação de métricas por estado

### 7. Dados Completos por Estado
- Tabela com todos os 27 estados
- Classificação por razão (do menor para o maior)
- Colunas: posição, estado, razão, homens 10k+, solteiros, mulheres solteiras, % empregados

### 8. Conclusão
- Síntese dos principais achados
- Implicações sociais e econômicas
- Limitações da análise
- Contexto sobre preferências pessoais vs. realidade estatística

### 9. Anexo Técnico
- Especificações completas das tabelas SIDRA utilizadas
- Parâmetros de análise (renda mínima, SM, faixa etária, etc.)
- Ferramentas e bibliotecas utilizadas
- Links para repositório e site público

## 🎨 Características de Design

O relatório utiliza:

- **Cores temáticas:** Vermelho primário (#e94560) e azul secundário (#2d4059)
- **Tabelas profissionais:** Headers coloridos, linhas alternadas, grid sutil
- **Destaques visuais:** Métricas importantes em destaque, cores para indicar melhores/piores
- **Numeração de páginas:** Automática, com rodapé contendo fonte dos dados
- **Espaçamento adequado:** Para facilitar leitura
- **Tipografia clara:** Helvetica, com variações de peso para hierarquia

## 🔧 Personalização

Para customizar o relatório, edite `gerar_relatorio_pdf.py`:

### Alterar cores

```python
# Procure por estas constantes no início do arquivo:
COR_PRIMARIA = colors.HexColor("#e94560")  # Sua cor principal
COR_SECUNDARIA = colors.HexColor("#2d4059")  # Sua cor secundária
COR_FUNDO_TABELA = colors.HexColor("#f5f5f5")  # Fundo de tabelas
```

### Alterar tamanho da página

```python
# Na função main(), procure por:
doc = SimpleDocTemplate(
    OUTPUT_PDF,
    pagesize=letter,  # Altere para A4, legal, etc.
    ...
)
```

### Modificar nome do arquivo

```python
# No início do arquivo:
OUTPUT_PDF = "relatorio_10k_ou_nada.pdf"  # Altere o nome aqui
```

### Adicionar/remover seções

Na função `main()`, comente ou adicione chamadas de função:

```python
# Construir relatório
criar_capa(story, styles)
criar_introducao(story, styles)
criar_metodologia(story, styles)
# criar_nova_secao(story, styles)  # Adicione sua seção aqui
```

## 🐛 Solução de Problemas

### Erro: "Arquivo não encontrado"

```
ERRO: Arquivo web/data/funil_nacional.json não encontrado.
```

**Solução:** Execute `python run_pipeline.py` primeiro para gerar os dados.

### Erro: "ModuleNotFoundError: No module named 'reportlab'"

**Solução:** Instale as dependências:
```bash
pip install reportlab kaleido
```

### Erro: Gráficos não aparecem no PDF

**Causa:** `kaleido` pode ter problemas em alguns ambientes.

**Solução:** O script já tem fallback - continua sem gráficos. Para forçar inclusão:
```bash
pip install --upgrade kaleido
```

### PDF parece "quebrado" ou malformatado

**Causa:** Dados muito grandes ou caracteres especiais.

**Solução:** Verifique os arquivos JSON - eles devem estar bem formatados e com encoding UTF-8.

## 📊 Tamanho e Performance

- **Tamanho típico:** 60-70 KB (sem imagens de gráficos)
- **Tempo de geração:** 5-15 segundos
- **Número de páginas:** 10-15 páginas
- **Formato:** PDF/A compatível, pode ser aberto em qualquer leitor

## 🔐 Compartilhamento

O relatório PDF é ideal para:

- ✅ Email (tamanho pequeno)
- ✅ Impressão (layout profissional)
- ✅ Apresentações (exportável)
- ✅ Arquivo (formato estável)
- ✅ Upload para repositórios acadêmicos

## 📝 Citação

Se você usar este relatório em trabalhos acadêmicos ou profissionais:

```
Jefferson M. F. (2026). R$ 10k ou nada? Análise quantitativa do mercado de 
trabalho brasileiro baseada em dados do Censo Demográfico 2022. 
Disponível em: https://github.com/JeffersonMFti/o_homem_provedor
```

## 🤝 Contribuindo

Para melhorar o gerador de relatórios:

1. Edite `gerar_relatorio_pdf.py`
2. Teste com `python gerar_relatorio_pdf.py`
3. Verifique o PDF gerado
4. Faça um pull request com sua melhoria

## 📮 Suporte

Problemas ou dúvidas? Abra uma issue no GitHub: 
https://github.com/JeffersonMFti/o_homem_provedor/issues

---

**📄 Última atualização:** Fevereiro 2026

"""
Script para gerar relatório completo em PDF do projeto "R$ 10k ou nada?"

Uso:
    python gerar_relatorio_pdf.py
    
Saída:
    relatorio_10k_ou_nada.pdf
"""

import sys
sys.path.insert(0, ".")

import json
import pandas as pd
from datetime import datetime
from pathlib import Path

# Importar módulos do projeto
from src.analyze import calcular_funil_nacional, calcular_funil_por_uf
from src.visualize import (
    grafico_distribuicao_renda,
    grafico_funil,
    grafico_barras_uf,
)
from config import DATA_PROCESSED, WEB_DATA

# Importar bibliotecas para PDF
try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4, letter
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch, cm
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
        PageBreak, Image, KeepTogether
    )
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
    from reportlab.pdfgen import canvas
except ImportError:
    print("ERRO: reportlab não está instalado.")
    print("Execute: pip install reportlab")
    sys.exit(1)

# Constantes
OUTPUT_PDF = "relatorio_10k_ou_nada.pdf"
TEMP_DIR = Path("temp_report_images")
TEMP_DIR.mkdir(exist_ok=True)

# Cores do projeto
COR_PRIMARIA = colors.HexColor("#e94560")
COR_SECUNDARIA = colors.HexColor("#2d4059")
COR_FUNDO_TABELA = colors.HexColor("#f5f5f5")


class NumberedCanvas(canvas.Canvas):
    """Canvas customizado para adicionar número de páginas e rodapé."""
    
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.grey)
        page_num = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(letter[0] - 1*cm, 1*cm, page_num)
        
        # Rodapé
        self.drawString(1*cm, 1*cm, "Fonte: Censo Demográfico 2022 - IBGE")


def criar_estilos():
    """Cria estilos customizados para o documento."""
    styles = getSampleStyleSheet()
    
    # Título principal
    styles.add(ParagraphStyle(
        name='CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=COR_SECUNDARIA,
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    ))
    
    # Subtítulo
    styles.add(ParagraphStyle(
        name='CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.grey,
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica'
    ))
    
    # Seção
    styles.add(ParagraphStyle(
        name='CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=COR_PRIMARIA,
        spaceAfter=12,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    ))
    
    # Texto normal com justificação
    styles.add(ParagraphStyle(
        name='Justify',
        parent=styles['BodyText'],
        alignment=TA_JUSTIFY,
        fontSize=11,
        leading=14
    ))
    
    # Destaque
    styles.add(ParagraphStyle(
        name='Destaque',
        parent=styles['BodyText'],
        fontSize=12,
        textColor=colors.HexColor('#2d2d2d'),
        fontName='Helvetica-Bold',
        spaceAfter=10,
        spaceBefore=10,
        alignment=TA_CENTER,
        leading=18
    ))
    
    # Box destacado
    styles.add(ParagraphStyle(
        name='BoxDestaque',
        parent=styles['BodyText'],
        fontSize=14,
        textColor=colors.HexColor('#2d4059'),
        fontName='Helvetica-Bold',
        spaceAfter=12,
        spaceBefore=12,
        alignment=TA_CENTER,
        leading=20,
        borderWidth=2,
        borderColor=COR_PRIMARIA,
        borderPadding=10
    ))
    
    return styles


def criar_capa(story, styles):
    """Cria a capa do relatório."""
    story.append(Spacer(1, 1.5*inch))
    
    # Título principal com destaque
    titulo = Paragraph(
        '<font size=28 color="#e94560"><b>R$ 10k ou nada?</b></font>',
        styles['CustomTitle']
    )
    story.append(titulo)
    story.append(Spacer(1, 0.2*inch))
    
    # Frase de efeito em caixa destacada
    frase = Paragraph(
        '<i><font size=13 color="#444444">"Pra namorar comigo, ele precisa ganhar pelo menos 10 mil por mês."</font></i>',
        styles['CustomSubtitle']
    )
    story.append(frase)
    story.append(Spacer(1, 0.4*inch))
    
    # Subtítulo
    subtitulo = Paragraph(
        'Análise quantitativa do mercado de trabalho brasileiro<br/>baseada em dados do Censo Demográfico 2022',
        styles['CustomSubtitle']
    )
    story.append(subtitulo)
    
    story.append(Spacer(1, 1*inch))
    
    # Informações do relatório
    info_data = [
        ['Fonte:', 'Censo Demográfico 2022 - IBGE'],
        ['Tabelas SIDRA:', '10292, 10185, 10268'],
        ['Data do relatório:', datetime.now().strftime('%d/%m/%Y')],
        ['Ano de referência:', '2022'],
    ]
    
    info_table = Table(info_data, colWidths=[2*inch, 4*inch])
    info_table.setStyle(TableStyle([
        ('FONT', (0, 0), (-1, -1), 'Helvetica', 10),
        ('FONT', (0, 0), (0, -1), 'Helvetica-Bold', 10),
        ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('TEXTCOLOR', (0, 0), (0, -1), COR_SECUNDARIA),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LINEBELOW', (0, 0), (-1, -1), 0.5, colors.lightgrey),
    ]))
    
    story.append(info_table)
    story.append(PageBreak())


def criar_introducao(story, styles):
    """Cria a seção de introdução."""
    story.append(Paragraph('1. Introdução', styles['CustomHeading']))
    
    texto = """
    Este relatório apresenta uma análise quantitativa do mercado de trabalho brasileiro 
    com foco em uma pergunta que viralizou nas redes sociais: <b>qual é a proporção real de 
    homens que ganham R$ 10.000 ou mais por mês no Brasil?</b>
    """
    story.append(Paragraph(texto, styles['Justify']))
    story.append(Spacer(1, 0.2*inch))
    
    texto2 = """
    A análise utiliza exclusivamente dados públicos do Censo Demográfico 2022, 
    realizado pelo IBGE, e busca responder três questões fundamentais:
    """
    story.append(Paragraph(texto2, styles['Justify']))
    story.append(Spacer(1, 0.1*inch))
    
    questoes = [
        '<b>1)</b> Qual percentual dos homens empregados ganha R$ 10.000 ou mais?',
        '<b>2)</b> Destes, quantos estão solteiros e potencialmente "disponíveis"?',
        '<b>3)</b> Qual a razão entre mulheres solteiras e homens solteiros de alta renda?',
    ]
    
    for q in questoes:
        story.append(Paragraph(f'• {q}', styles['BodyText']))
    
    story.append(Spacer(1, 0.2*inch))
    
    texto3 = """
    O objetivo não é julgar preferências individuais, mas sim contextualizar expectativas 
    com a realidade do mercado de trabalho nacional, revelando disparidades regionais 
    e socioeconômicas importantes.
    """
    story.append(Paragraph(texto3, styles['Justify']))
    story.append(Spacer(1, 0.3*inch))


def criar_metodologia(story, styles):
    """Cria a seção de metodologia."""
    story.append(Paragraph('2. Metodologia', styles['CustomHeading']))
    
    texto = """
    A análise foi estruturada em quatro etapas sequenciais, cada uma refinando o universo 
    populacional de interesse:
    """
    story.append(Paragraph(texto, styles['Justify']))
    story.append(Spacer(1, 0.15*inch))
    
    # Tabela de etapas com quebra de linha melhorada
    etapas_data = [
        ['Etapa', 'Descrição', 'Fonte'],
        ['1. Renda', 
         Paragraph('Estimativa de homens com renda ≥ R$ 10.000/mês a partir de faixas de salário mínimo', styles['BodyText']),
         'Tabela\n10292'],
        ['2. Estado\nconjugal',
         Paragraph('Taxa de homens sem união conjugal (25-44 anos) aplicada como proxy ao grupo de alta renda', styles['BodyText']),
         'Tabela\n10185'],
        ['3. Mulheres\nsolteiras',
         Paragraph('Contagem de mulheres sem união conjugal na mesma faixa etária para cálculo da razão', styles['BodyText']),
         'Tabela\n10185'],
        ['4. Razão\nfinal',
         Paragraph('Cálculo da razão: mulheres solteiras dividido por homens solteiros com R$ 10k+', styles['BodyText']),
         'Calculado'],
    ]
    
    etapas_table = Table(etapas_data, colWidths=[1*inch, 3.8*inch, 1*inch])
    etapas_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COR_SECUNDARIA),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('ALIGN', (2, 0), (2, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 11),
        ('FONT', (0, 1), (0, -1), 'Helvetica-Bold', 10),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COR_FUNDO_TABELA]),
    ]))
    
    story.append(etapas_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Limitações
    story.append(Paragraph('<b>Limitações metodológicas:</b>', styles['BodyText']))
    story.append(Spacer(1, 0.1*inch))
    
    limitacoes = [
        'A renda é declarada em faixas de salário mínimo. Para estimar homens acima de R$ 10k dentro da faixa "5 a 10 SM", utilizou-se interpolação linear.',
        'A taxa de solteiros (25-44 anos) é aplicada como proxy ao grupo de alta renda, pois o Censo não publica o cruzamento direto renda × estado conjugal × faixa etária.',
        '"Solteiro" significa "não vivia em união conjugal", incluindo solteiros, divorciados e viúvos.',
        'Análise limitada ao mercado formal de trabalho (carteira assinada ou emprego público).',
    ]
    
    for lim in limitacoes:
        story.append(Paragraph(f'• {lim}', styles['BodyText']))
    
    story.append(Spacer(1, 0.3*inch))


def criar_resultados_nacionais(story, styles, funil):
    """Cria a seção de resultados nacionais."""
    story.append(Paragraph('3. Resultados Nacionais', styles['CustomHeading']))
    
    # Resumo executivo em caixa destacada
    resumo_texto = f"""
    <b>Do total de {funil['homens_empregados']:,} homens empregados no Brasil, 
    apenas {funil['pct_homens_10k']:.2f}% ({funil['homens_10k']:,}) ganham R$ 10.000 ou mais por mês.</b>
    """
    
    resumo_table = Table([[Paragraph(resumo_texto.replace(',', '.'), styles['Destaque'])]], colWidths=[5.5*inch])
    resumo_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#ffe6ea')),
        ('BORDER', (0, 0), (-1, -1), 2, COR_PRIMARIA),
        ('PADDING', (0, 0), (-1, -1), 15),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))
    
    story.append(resumo_table)
    story.append(Spacer(1, 0.25*inch))
    
    # Tabela de métricas principais
    metricas_data = [
        ['Indicador', 'Valor', '% do anterior'],
        ['Homens empregados (total)', f"{funil['homens_empregados']:,}".replace(',', '.'), '100%'],
        ['💰 Ganham R$ 10k+', f"{funil['homens_10k']:,}".replace(',', '.'), f"{funil['pct_homens_10k']:.2f}%"],
        ['💑 Destes, estão solteiros', f"{funil['homens_10k_solteiros']:,}".replace(',', '.'), f"{funil['taxa_solteiros']*100:.1f}%"],
        ['👥 Mulheres solteiras (25-44 anos)', f"{funil['mulheres_solteiras']:,}".replace(',', '.'), '—'],
        ['📊 Razão (mulheres/homens)', f"{funil['razao']:.1f}x", '—'],
    ]
    
    metricas_table = Table(metricas_data, colWidths=[3*inch, 1.5*inch, 1.3*inch])
    metricas_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COR_PRIMARIA),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 11),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 11),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COR_FUNDO_TABELA]),
        ('FONT', (0, 2), (-1, 2), 'Helvetica-Bold', 11),
        ('BACKGROUND', (0, 2), (-1, 2), colors.HexColor('#ffe6ea')),
        ('LINEABOVE', (0, 2), (-1, 2), 2, COR_PRIMARIA),
    ]))
    
    story.append(metricas_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Interpretação
    interpretacao = f"""
    Estes números revelam que <b>para cada homem solteiro que ganha R$ 10.000 ou mais, 
    existem aproximadamente {funil['razao']:.0f} mulheres solteiras</b> na mesma faixa etária (25-44 anos). 
    Este é um indicador do desequilíbrio entre expectativa e oferta disponível no "mercado" 
    de parceiros com essa característica econômica específica.
    """
    story.append(Paragraph(interpretacao, styles['Justify']))
    story.append(Spacer(1, 0.3*inch))


def adicionar_grafico_plotly(story, fig, filename, width=6*inch, caption=None):
    """Salva um gráfico Plotly como imagem e adiciona ao relatório."""
    try:
        # Atualizar layout do gráfico para melhor legibilidade no PDF
        fig.update_layout(
            font=dict(size=16, color='#2d2d2d', family='Arial, sans-serif'),
            title=dict(font=dict(size=20, color='#2d4059')),
            xaxis=dict(
                tickfont=dict(size=14, color='#2d2d2d'),
                title=dict(font=dict(size=16, color='#2d2d2d'))
            ),
            yaxis=dict(
                tickfont=dict(size=14, color='#2d2d2d'),
                title=dict(font=dict(size=16, color='#2d2d2d'))
            ),
            legend=dict(font=dict(size=14, color='#2d2d2d')),
        )
        
        # Salvar como imagem em alta resolução
        img_path = TEMP_DIR / filename
        fig.write_image(str(img_path), width=1400, height=800, scale=2)
        
        # Adicionar ao PDF
        img = Image(str(img_path), width=width, height=width*800/1400)
        story.append(img)
        
        if caption:
            caption_style = ParagraphStyle(
                'Caption',
                parent=getSampleStyleSheet()['BodyText'],
                fontSize=9,
                textColor=colors.grey,
                alignment=TA_CENTER,
                spaceAfter=12
            )
            story.append(Spacer(1, 0.1*inch))
            story.append(Paragraph(caption, caption_style))
            
    except Exception as e:
        print(f"Aviso: Não foi possível adicionar gráfico {filename}. Erro: {e}")
        print("      Tentando usar método alternativo...")
        
        # Fallback: adicionar placeholder
        texto = f"[Gráfico: {caption if caption else filename}]"
        story.append(Paragraph(texto, getSampleStyleSheet()['BodyText']))
    
    story.append(Spacer(1, 0.2*inch))


def criar_distribuicao_renda(story, styles):
    """Cria a seção de distribuição de renda."""
    story.append(PageBreak())
    story.append(Paragraph('4. Distribuição de Renda', styles['CustomHeading']))
    
    texto = """
    A tabela abaixo apresenta a distribuição completa dos homens empregados por faixa de renda,
    em salários mínimos (SM). Observe como a concentração em faixas inferiores é predominante,
    com mais de 60% ganhando até 2 SM (aproximadamente R$ 2.424).
    """
    story.append(Paragraph(texto, styles['Justify']))
    story.append(Spacer(1, 0.2*inch))
    
    # Carregar dados de distribuição
    with open(WEB_DATA / 'distribuicao_renda.json', 'r', encoding='utf-8') as f:
        distribuicao = json.load(f)
    
    # Criar tabela de distribuição
    dist_data = [['Faixa de Renda (SM)', 'Homens', '% do Total', '10k+']]
    
    for item in distribuicao:
        pessoas = f"{item['pessoas']:,}".replace(',', '.')
        pct = f"{item['pct']:.1f}%"
        acima = '✓' if item['acima_threshold'] else ''
        dist_data.append([item['classe_sm'], pessoas, pct, acima])
    
    dist_table = Table(dist_data, colWidths=[2.8*inch, 1.3*inch, 1*inch, 0.8*inch])
    dist_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COR_SECUNDARIA),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 10),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 9),
        ('GRID', (0, 0), (-1, -1), 0.8, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COR_FUNDO_TABELA]),
    ]))
    
    # Destacar linhas acima do threshold
    for i, item in enumerate(distribuicao, start=1):
        if item['acima_threshold']:
            dist_table.setStyle(TableStyle([
                ('BACKGROUND', (0, i), (-1, i), colors.HexColor('#ffe6ea')),
                ('FONT', (0, i), (-1, i), 'Helvetica-Bold', 9),
            ]))
    
    story.append(dist_table)
    story.append(Spacer(1, 0.2*inch))
    
    # Tentar adicionar gráfico
    try:
        with open(WEB_DATA / 'distribuicao_renda.json', 'r', encoding='utf-8') as f:
            dist_df = pd.DataFrame(json.load(f))
        
        fig = grafico_distribuicao_renda(dist_df)
        adicionar_grafico_plotly(
            story, fig, 'distribuicao_renda.png',
            caption='Figura 1: Distribuição de homens empregados por faixa de renda'
        )
    except Exception as e:
        print(f"Não foi possível adicionar gráfico de distribuição: {e}")


def criar_analise_estados(story, styles, df_uf):
    """Cria a seção de análise por estados."""
    story.append(PageBreak())
    story.append(Paragraph('5. Análise por Estado', styles['CustomHeading']))
    
    texto = """
    A disparidade regional é um fator crítico nesta análise. Estados com maior concentração
    de empregos formais bem remunerados apresentam razões significativamente menores.
    O Distrito Federal, por exemplo, tem a menor razão do país, enquanto estados do
    Norte e Nordeste apresentam as maiores.
    """
    story.append(Paragraph(texto, styles['Justify']))
    story.append(Spacer(1, 0.2*inch))
    
    # Top 5 melhores e piores
    df_sorted = df_uf.sort_values('razao')
    
    story.append(Paragraph('✅ <b>Estados com menor razão (mais homens de alta renda por mulher):</b>', 
                          styles['BodyText']))
    story.append(Spacer(1, 0.1*inch))
    
    top5_data = [['Estado', 'Razão', 'Homens R$ 10k+', '% Empregados']]
    for _, row in df_sorted.head(5).iterrows():
        top5_data.append([
            row['uf'],
            f"{row['razao']:.1f}x",
            f"{int(row['homens_10k']):,}".replace(',', '.'),
            f"{row['pct_homens_10k']:.1f}%"
        ])
    
    top5_table = Table(top5_data, colWidths=[2*inch, 1*inch, 1.5*inch, 1.3*inch])
    top5_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E7D32')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 11),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#C8E6C9')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#E8F5E9'), colors.HexColor('#C8E6C9')]),
    ]))
    
    story.append(top5_table)
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph('❌ <b>Estados com maior razão (menos homens de alta renda por mulher):</b>', 
                          styles['BodyText']))
    story.append(Spacer(1, 0.1*inch))
    
    bottom5_data = [['Estado', 'Razão', 'Homens R$ 10k+', '% Empregados']]
    for _, row in df_sorted.tail(5).iterrows():
        bottom5_data.append([
            row['uf'],
            f"{row['razao']:.1f}x",
            f"{int(row['homens_10k']):,}".replace(',', '.'),
            f"{row['pct_homens_10k']:.1f}%"
        ])
    
    bottom5_table = Table(bottom5_data, colWidths=[2*inch, 1*inch, 1.5*inch, 1.3*inch])
    bottom5_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#C62828')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 11),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#FFCDD2')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#FFEBEE'), colors.HexColor('#FFCDD2')]),
    ]))
    
    story.append(bottom5_table)
    story.append(Spacer(1, 0.3*inch))


def criar_tabela_completa_estados(story, styles, df_uf):
    """Cria tabela completa com todos os estados."""
    story.append(PageBreak())
    story.append(Paragraph('6. Dados Completos por Estado', styles['CustomHeading']))
    
    # Ordenar por razão crescente
    df_sorted = df_uf.sort_values('razao').reset_index(drop=True)
    
    # Tabela completa
    tabela_data = [['#', 'Estado', 'Razão', 'Homens 10k+', 'Solteiros', 'Mulheres Solt.', '% Emp.']]
    
    for i, row in df_sorted.iterrows():
        tabela_data.append([
            str(i+1),
            row['uf'],
            f"{row['razao']:.1f}",
            f"{int(row['homens_10k']):,}".replace(',', '.'),
            f"{int(row['homens_10k_solteiros']):,}".replace(',', '.'),
            f"{int(row['mulheres_solteiras']):,}".replace(',', '.'),
            f"{row['pct_homens_10k']:.1f}"
        ])
    
    tabela_completa = Table(tabela_data, 
                            colWidths=[0.3*inch, 1.5*inch, 0.7*inch, 1*inch, 1*inch, 1.2*inch, 0.6*inch])
    tabela_completa.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COR_SECUNDARIA),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (1, -1), 'LEFT'),
        ('ALIGN', (2, 0), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 8),
        ('FONT', (0, 1), (-1, -1), 'Helvetica', 7),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COR_FUNDO_TABELA]),
    ]))
    
    story.append(tabela_completa)
    story.append(Spacer(1, 0.3*inch))


def criar_conclusao(story, styles, funil):
    """Cria a seção de conclusão."""
    story.append(PageBreak())
    story.append(Paragraph('7. Conclusão', styles['CustomHeading']))
    
    texto1 = f"""
    Os dados são inequívocos: <b>homens que ganham R$ 10.000 ou mais por mês representam 
    apenas {funil['pct_homens_10k']:.1f}% do mercado formal de trabalho brasileiro</b>. 
    Quando consideramos apenas os solteiros, o número cai para aproximadamente 
    {funil['homens_10k_solteiros']:,} indivíduos em todo o país.
    """.replace(',', '.')
    story.append(Paragraph(texto1, styles['Justify']))
    story.append(Spacer(1, 0.15*inch))
    
    texto2 = f"""
    A razão nacional de {funil['razao']:.0f} mulheres solteiras para cada homem solteiro 
    nessa faixa de renda evidencia um desequilíbrio significativo entre expectativa e 
    disponibilidade. Esta disparidade é ainda mais acentuada em estados do Norte e Nordeste, 
    onde a razão pode ultrapassar 30:1.
    """
    story.append(Paragraph(texto2, styles['Justify']))
    story.append(Spacer(1, 0.15*inch))
    
    texto3 = """
    <b>Implicações principais:</b>
    """
    story.append(Paragraph(texto3, styles['BodyText']))
    story.append(Spacer(1, 0.1*inch))
    
    implicacoes = [
        'A concentração de renda no Brasil cria uma competição assimétrica por parceiros de alta renda, especialmente em regiões economicamente menos desenvolvidas.',
        'Expectativas moldadas por nichos específicos (grandes capitais, setores como tecnologia e finanças) não refletem a realidade nacional.',
        'A análise reforça a importância de políticas públicas voltadas à geração de empregos formais de qualidade e redução da desigualdade regional.',
        'Do ponto de vista individual, os dados sugerem que critérios exclusivamente econômicos podem limitar significativamente o universo de parceiros potenciais.',
    ]
    
    for imp in implicacoes:
        story.append(Paragraph(f'• {imp}', styles['BodyText']))
    
    story.append(Spacer(1, 0.2*inch))
    
    texto4 = """
    <b>É fundamental ressaltar que esta análise não pretende julgar preferências pessoais</b>, 
    mas sim contextualizar expectativas com dados concretos da realidade brasileira. 
    Decisões sobre relacionamentos envolvem múltiplos fatores além de renda, e cada 
    indivíduo tem o direito de estabelecer seus próprios critérios.
    """
    story.append(Paragraph(texto4, styles['Justify']))
    story.append(Spacer(1, 0.15*inch))
    
    texto5 = """
    O que os dados mostram, de forma objetiva, é que a expectativa de um parceiro com 
    renda de R$ 10.000+ está estatisticamente distante da realidade do mercado de trabalho 
    brasileiro, especialmente fora dos grandes centros urbanos.
    """
    story.append(Paragraph(texto5, styles['Justify']))
    story.append(Spacer(1, 0.3*inch))


def criar_anexo_tecnico(story, styles):
    """Cria anexo técnico com detalhes das fontes."""
    story.append(PageBreak())
    story.append(Paragraph('Anexo: Especificações Técnicas', styles['CustomHeading']))
    
    # Tabelas SIDRA utilizadas
    story.append(Paragraph('<b>Fontes de dados (Tabelas SIDRA/IBGE):</b>', styles['BodyText']))
    story.append(Spacer(1, 0.15*inch))
    
    # Estilo para células da tabela
    cell_style = ParagraphStyle(
        'CellStyle',
        parent=styles['BodyText'],
        fontSize=9,
        leading=11,
        alignment=TA_LEFT
    )
    
    tabelas_data = [
        [
            Paragraph('<b>Tabela</b>', styles['BodyText']),
            Paragraph('<b>Descrição</b>', styles['BodyText']),
            Paragraph('<b>Variáveis Utilizadas</b>', styles['BodyText'])
        ],
        [
            Paragraph('10292', cell_style),
            Paragraph('Pessoas de 14 anos ou mais de idade, ocupadas na semana de referência, por classes de rendimento nominal mensal do trabalho principal', cell_style),
            Paragraph('Sexo, Faixas de SM, UF', cell_style)
        ],
        [
            Paragraph('10185', cell_style),
            Paragraph('Pessoas de 14 anos ou mais de idade, por grupos de idade e estado conjugal', cell_style),
            Paragraph('Sexo, Faixa etária 25-44, Estado conjugal, UF', cell_style)
        ],
        [
            Paragraph('10268', cell_style),
            Paragraph('População residente, por sexo e grupos de idade', cell_style),
            Paragraph('Sexo, Grupos de idade, UF', cell_style)
        ],
    ]
    
    tabelas_table = Table(tabelas_data, colWidths=[0.7*inch, 3.3*inch, 1.8*inch])
    tabelas_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COR_SECUNDARIA),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold', 10),
        ('GRID', (0, 0), (-1, -1), 0.8, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, COR_FUNDO_TABELA]),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    
    story.append(tabelas_table)
    story.append(Spacer(1, 0.25*inch))
    
    # Parâmetros de análise
    story.append(Paragraph('<b>Parâmetros de análise:</b>', styles['BodyText']))
    story.append(Spacer(1, 0.12*inch))
    
    # Criar tabela de parâmetros para melhor formatação
    param_style = ParagraphStyle(
        'ParamStyle',
        parent=styles['BodyText'],
        fontSize=10,
        leading=13
    )
    
    parametros_data = [
        [Paragraph('• <b>Renda mínima:</b>', param_style), Paragraph('R$ 10.000,00 mensais', param_style)],
        [Paragraph('• <b>Salário mínimo de referência (2022):</b>', param_style), Paragraph('R$ 1.212,00', param_style)],
        [Paragraph('• <b>Faixa etária considerada:</b>', param_style), Paragraph('25 a 44 anos', param_style)],
        [Paragraph('• <b>Método de interpolação:</b>', param_style), Paragraph('Linear dentro da faixa 5-10 SM', param_style)],
        [Paragraph('• <b>Definição de "solteiro":</b>', param_style), Paragraph('Sem união conjugal (inclui solteiros, divorciados e viúvos)', param_style)],
    ]
    
    param_table = Table(parametros_data, colWidths=[2.5*inch, 3.3*inch])
    param_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    
    story.append(param_table)
    story.append(Spacer(1, 0.25*inch))
    
    # Ferramentas utilizadas
    story.append(Paragraph('<b>Ferramentas e bibliotecas:</b>', styles['BodyText']))
    story.append(Spacer(1, 0.12*inch))
    
    ferramentas_data = [
        [Paragraph('• <b>Coleta de dados:</b>', param_style), Paragraph('sidrapy (API SIDRA/IBGE)', param_style)],
        [Paragraph('• <b>Processamento:</b>', param_style), Paragraph('Python 3.x, pandas, numpy', param_style)],
        [Paragraph('• <b>Visualizações:</b>', param_style), Paragraph('Plotly, matplotlib', param_style)],
        [Paragraph('• <b>Geração de relatório:</b>', param_style), Paragraph('ReportLab', param_style)],
        [Paragraph('• <b>Controle de versão:</b>', param_style), Paragraph('Git / GitHub', param_style)],
    ]
    
    ferram_table = Table(ferramentas_data, colWidths=[2.2*inch, 3.6*inch])
    ferram_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    
    story.append(ferram_table)
    story.append(Spacer(1, 0.25*inch))
    
    # Links do projeto
    story.append(Paragraph('<b>Links do projeto:</b>', styles['BodyText']))
    story.append(Spacer(1, 0.12*inch))
    
    links_data = [
        [Paragraph('• <b>Repositório:</b>', param_style), 
         Paragraph('<link href="https://github.com/JeffersonMFti/o_homem_provedor" color="blue">github.com/JeffersonMFti/o_homem_provedor</link>', param_style)],
        [Paragraph('• <b>Site público:</b>', param_style), 
         Paragraph('<link href="https://o-homem-provedor.vercel.app" color="blue">o-homem-provedor.vercel.app</link>', param_style)],
    ]
    
    links_table = Table(links_data, colWidths=[1.5*inch, 4.3*inch])
    links_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    
    story.append(links_table)


def main():
    """Função principal para gerar o relatório."""
    print("=" * 60)
    print("Gerador de Relatório PDF - Projeto R$ 10k ou nada?")
    print("=" * 60)
    print()
    
    # Verificar se os dados existem
    print("[1/7] Verificando dados...")
    required_files = [
        WEB_DATA / 'funil_nacional.json',
        WEB_DATA / 'funil_por_estado.json',
        WEB_DATA / 'distribuicao_renda.json',
    ]
    
    for filepath in required_files:
        if not filepath.exists():
            print(f"ERRO: Arquivo {filepath} não encontrado.")
            print("Execute 'python run_pipeline.py' primeiro para gerar os dados.")
            sys.exit(1)
    
    print("   ✓ Todos os arquivos de dados encontrados")
    
    # Carregar dados
    print("[2/7] Carregando dados...")
    with open(WEB_DATA / 'funil_nacional.json', 'r', encoding='utf-8') as f:
        funil = json.load(f)
    
    with open(WEB_DATA / 'funil_por_estado.json', 'r', encoding='utf-8') as f:
        df_uf = pd.DataFrame(json.load(f))
    
    print(f"   ✓ Dados carregados: {len(df_uf)} estados")
    
    # Criar documento PDF
    print("[3/7] Criando estrutura do documento...")
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72,
    )
    
    story = []
    styles = criar_estilos()
    
    # Construir relatório
    print("[4/7] Gerando capa e introdução...")
    criar_capa(story, styles)
    criar_introducao(story, styles)
    
    print("[5/7] Gerando seções de metodologia e resultados...")
    criar_metodologia(story, styles)
    criar_resultados_nacionais(story, styles, funil)
    criar_distribuicao_renda(story, styles)
    
    print("[6/7] Gerando análise por estados...")
    criar_analise_estados(story, styles, df_uf)
    criar_tabela_completa_estados(story, styles, df_uf)
    
    print("[7/7] Finalizando relatório...")
    criar_conclusao(story, styles, funil)
    criar_anexo_tecnico(story, styles)
    
    # Gerar PDF
    print()
    print("Gerando arquivo PDF...")
    doc.build(story, canvasmaker=NumberedCanvas)
    
    print()
    print("=" * 60)
    print(f"✓ Relatório gerado com sucesso: {OUTPUT_PDF}")
    print(f"  Tamanho: {Path(OUTPUT_PDF).stat().st_size / 1024:.1f} KB")
    print("=" * 60)
    
    # Limpar arquivos temporários
    try:
        import shutil
        if TEMP_DIR.exists():
            shutil.rmtree(TEMP_DIR)
            print("  (Arquivos temporários removidos)")
    except:
        pass


if __name__ == "__main__":
    main()

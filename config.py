from pathlib import Path

ROOT = Path(__file__).parent

DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
WEB_DATA = ROOT / "web" / "data"

FAIXA_ETARIA = [
    "25 a 29 anos",
    "30 a 34 anos",
    "35 a 39 anos",
    "40 a 44 anos",
]

RENDA_MINIMA = 10_000
ANO_REFERENCIA = 2022  # Censo Demográfico 2022

SEXO_MASCULINO = "Homens"
SEXO_FEMININO = "Mulheres"
ESTADO_CONJUGAL_SEM_UNIAO = "Não viviam em união"

# Salário mínimo vigente no Censo 2022 (usado para converter SM em R$)
SALARIO_MINIMO_CENSO = 1_212

# Tabelas do Censo Demográfico 2022 utilizadas (via SIDRA)
# Pessoas ocupadas por sexo e classes de rendimento em SM, por UF
CENSO_RENDA_SM = "10292"
# Pessoas por estado conjugal, sexo e grupo de idade, por UF
CENSO_CONJUGAL = "10185"
# Pessoas ocupadas por sexo e grupo de idade, por UF
CENSO_OCUPADOS_FAIXA = "10268"

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
ANO_REFERENCIA = 2023

SEXO_MASCULINO = "Homens"
SEXO_FEMININO = "Mulheres"
ESTADO_CIVIL_SOLTEIRO = "Solteiro(a)"

# Tabelas SIDRA utilizadas
SIDRA_RENDA = "7439"
SIDRA_ESTADO_CIVIL = "5929"
SIDRA_RENDA_UF = "6403"

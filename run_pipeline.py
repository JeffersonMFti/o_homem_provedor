import argparse
import sys

sys.path.insert(0, ".")

from src.collect import buscar_renda_por_sm, buscar_estado_conjugal, buscar_ocupados_por_faixa
from src.process import processar_tudo
from src.analyze import calcular_funil_nacional, calcular_funil_por_uf
from src.export import (
    exportar_funil_nacional,
    exportar_funil_por_estado,
    exportar_distribuicao_renda,
    exportar_razao_por_uf,
)
from config import DATA_PROCESSED


def _step_collect():
    print("[collect]")
    buscar_renda_por_sm()
    buscar_estado_conjugal()
    buscar_ocupados_por_faixa()


def _step_process():
    print("[process]")
    processar_tudo()


def _step_analyze():
    print("[analyze]")
    funil = calcular_funil_nacional()
    df_uf = calcular_funil_por_uf()
    print(f"   Razao nacional: {funil['razao']}")
    return funil, df_uf


def _step_export(funil=None, df_uf=None):
    import pandas as pd

    print("[export]")
    if funil is None:
        funil = calcular_funil_nacional()
    if df_uf is None:
        df_uf = calcular_funil_por_uf()

    renda = pd.read_csv(DATA_PROCESSED / "renda_por_sm.csv", encoding="utf-8")

    exportar_funil_nacional(funil)
    exportar_funil_por_estado(df_uf)
    exportar_distribuicao_renda(renda)
    exportar_razao_por_uf(df_uf)
    print("   JSONs salvos em web/data/")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--step", choices=["collect", "process", "analyze", "export"])
    args = parser.parse_args()

    if args.step == "collect":
        _step_collect()
    elif args.step == "process":
        _step_process()
    elif args.step == "analyze":
        _step_analyze()
    elif args.step == "export":
        _step_export()
    else:
        _step_collect()
        _step_process()
        funil, df_uf = _step_analyze()
        _step_export(funil, df_uf)
        print("Pipeline concluido.")


if __name__ == "__main__":
    main()

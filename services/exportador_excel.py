import os

import pandas as pd

NOMBRE_ARCHIVO_EXCEL = "resultados_busqueda.xlsx"
NOMBRE_CARPETA_OUTPUT = "output"

COLUMNAS_EXCEL = [
    "termino_busqueda",
    "producto",
    "precio",
    "vendedor",
    "calificacion",
    "envio_gratis",
    "link",
]


def exportar_resultados(lista_resultados):
    dataframe = pd.DataFrame(lista_resultados)
    dataframe = dataframe[COLUMNAS_EXCEL]

    raiz_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    carpeta_output = os.path.join(raiz_proyecto, NOMBRE_CARPETA_OUTPUT)
    os.makedirs(carpeta_output, exist_ok=True)

    ruta_excel = os.path.join(carpeta_output, NOMBRE_ARCHIVO_EXCEL)
    dataframe.to_excel(ruta_excel, index=False)

    print(f"Se guardaron {len(lista_resultados)} resultados en {NOMBRE_ARCHIVO_EXCEL}")

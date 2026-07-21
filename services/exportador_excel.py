import os

import pandas as pd

from utils.config import Config
from utils.impresor import Impresor
from utils.logger import Logger

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

    os.makedirs(Config.ruta_carpeta_output(), exist_ok=True)

    try:
        dataframe.to_excel(Config.ruta_excel(), index=False)
    except Exception as error:
        Logger.error(f"No se pudo guardar el Excel: {error}")
        Impresor.aviso("No se pudo guardar el archivo Excel (¿está abierto en otro programa?)")
        return

    Impresor.mostrar(f"Se guardaron {len(lista_resultados)} resultados en {Config.NOMBRE_ARCHIVO_EXCEL}")

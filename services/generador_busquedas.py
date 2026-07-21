import json

from utils.config import Config
from utils.impresor import Impresor


def pedir_terminos_busqueda():
    while True:
        texto = input("Escribe los productos a buscar, separados por coma: ")

        if texto.strip() == "":
            Impresor.mostrar("No escribiste nada válido. Intenta de nuevo.")
            continue

        return texto.split(",")


def guardar_terminos(terminos):
    ruta_json = Config.ruta_json_busquedas()

    with open(ruta_json, "w", encoding="utf-8") as archivo:
        json.dump(terminos, archivo, ensure_ascii=False, indent=2)

    Impresor.mostrar(f"Se guardaron {len(terminos)} términos en {Config.NOMBRE_ARCHIVO_JSON}")


def generar_busquedas():
    terminos = pedir_terminos_busqueda()
    guardar_terminos(terminos)

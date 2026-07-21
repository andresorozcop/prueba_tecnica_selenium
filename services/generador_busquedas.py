import json
import os

NOMBRE_ARCHIVO = "productos_busqueda.json"


def pedir_terminos_busqueda():
    while True:
        texto = input("Escribe los productos a buscar, separados por coma: ")

        if texto.strip() == "":
            print("No escribiste nada válido. Intenta de nuevo.")
            continue

        return texto.split(",")


def guardar_terminos(terminos):
    raiz_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_json = os.path.join(raiz_proyecto, NOMBRE_ARCHIVO)

    with open(ruta_json, "w", encoding="utf-8") as archivo:
        json.dump(terminos, archivo, ensure_ascii=False, indent=2)

    print(f"Se guardaron {len(terminos)} términos en {NOMBRE_ARCHIVO}")


def generar_busquedas():
    terminos = pedir_terminos_busqueda()
    guardar_terminos(terminos)

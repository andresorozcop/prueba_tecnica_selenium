import json
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from services.extractor_resultados import extraer_cinco_resultados
from services.exportador_excel import exportar_resultados

NOMBRE_ARCHIVO = "productos_busqueda.json"
URL_MERCADOLIBRE = "https://www.mercadolibre.com.co"
NOMBRE_CARPETA_PERFIL = "chrome_profile"


def obtener_todos_los_terminos():
    raiz_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_json = os.path.join(raiz_proyecto, NOMBRE_ARCHIVO)

    with open(ruta_json, "r", encoding="utf-8") as archivo:
        terminos = json.load(archivo)

    return terminos


def crear_driver():
    raiz_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_perfil = os.path.join(raiz_proyecto, NOMBRE_CARPETA_PERFIL)

    # perfil persistente: así Chrome mantiene cookies/sesión entre corridas
    # en vez de verse como un usuario nuevo cada vez (evita bloqueos de ML)
    opciones = webdriver.ChromeOptions()
    opciones.add_argument(f"--user-data-dir={ruta_perfil}")

    servicio = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=servicio, options=opciones)


def buscar_en_mercadolibre(driver, termino):
    driver.get(URL_MERCADOLIBRE)

    campo_busqueda = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "as_word"))
    )
    campo_busqueda.send_keys(termino)
    campo_busqueda.send_keys(Keys.ENTER)

    # respaldo si aun así aparece el recaptcha: no seguimos hasta que el usuario confirme
    input("Si aparece un recaptcha, resuélvelo y presiona Enter para continuar...")

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ui-search-results"))
    )


def procesar_todas_las_busquedas():
    terminos = obtener_todos_los_terminos()

    driver = crear_driver()

    resultados_totales = []
    for termino in terminos:
        termino = termino.strip()
        print(f"Buscando término: {termino}")

        buscar_en_mercadolibre(driver, termino)

        resultados = extraer_cinco_resultados(driver)
        for resultado in resultados:
            resultado["termino_busqueda"] = termino
        resultados_totales.extend(resultados)

    exportar_resultados(resultados_totales)

    input("Presiona Enter para cerrar Chrome...")
    driver.quit()

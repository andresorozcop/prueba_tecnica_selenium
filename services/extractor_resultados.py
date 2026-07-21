from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

CANTIDAD_RESULTADOS = 5


def extraer_cinco_resultados(driver):
    tarjetas = driver.find_elements(By.CLASS_NAME, "poly-card")[:CANTIDAD_RESULTADOS]

    resultados = []
    for tarjeta in tarjetas:
        resultados.append(extraer_un_resultado(tarjeta))

    return resultados


def extraer_un_resultado(tarjeta):
    resultado = {
        "producto": "N/A",
        "precio": "N/A",
        "vendedor": "N/A",
        "calificacion": "N/A",
        "envio_gratis": "No",
        "link": "N/A",
    }

    try:
        elemento_titulo = tarjeta.find_element(By.CSS_SELECTOR, "h3 a.poly-component__title")
        resultado["producto"] = elemento_titulo.text
        resultado["link"] = elemento_titulo.get_attribute("href")
    except NoSuchElementException:
        print("[AVISO] Producto/Link no encontrado en un resultado")

    try:
        # si el producto tiene descuento, el precio actual vive dentro de poly-price__current
        try:
            elemento_precio = tarjeta.find_element(By.CSS_SELECTOR, ".poly-price__current .poly-price__amount")
        except NoSuchElementException:
            elemento_precio = tarjeta.find_element(By.CSS_SELECTOR, ".poly-price__amount")
        # el símbolo $ y el número quedan en spans separados, .text los junta con salto de línea
        resultado["precio"] = elemento_precio.text.replace("\n", " ")
    except NoSuchElementException:
        print(f"[AVISO] Precio no encontrado para: {resultado['producto']}")

    try:
        resultado["vendedor"] = tarjeta.find_element(By.CSS_SELECTOR, "span.poly-component__seller").text
    except NoSuchElementException:
        print(f"[AVISO] Vendedor no encontrado para: {resultado['producto']}")

    try:
        resultado["calificacion"] = tarjeta.find_element(
            By.CSS_SELECTOR, "span.poly-component__review-compacted .polylabel-label"
        ).text
    except NoSuchElementException:
        print(f"[AVISO] Calificación no encontrada para: {resultado['producto']}")

    # envío gratis no es un campo faltante, es Si/No según si existe el bloque
    try:
        tarjeta.find_element(By.CSS_SELECTOR, "div.poly-component__shipping-v2")
        resultado["envio_gratis"] = "Si"
    except NoSuchElementException:
        resultado["envio_gratis"] = "No"

    return resultado

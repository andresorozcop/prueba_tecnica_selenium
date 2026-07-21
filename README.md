# Automatización Mercado Libre

## Descripción

Proyecto en Python que automatiza búsquedas en Mercado Libre Colombia usando Selenium.
Por cada producto que se busque, extrae los primeros 5 resultados (nombre, precio,
vendedor, calificación, envío gratis y link) y consolida todo en un archivo Excel.

## Requisitos

- Python 3.10 o superior.
- Google Chrome instalado (el driver se descarga solo, no hay que instalarlo a mano).
- Conexión a internet.

## Instalación

1. Crear y activar un entorno virtual:

   ```
   python -m venv venv
   venv\Scripts\activate
   ```

2. Instalar las dependencias:

   ```
   pip install -r requirements.txt
   ```

3. Copiar `.env.example` a un archivo nuevo llamado `.env` (mismos valores por defecto,
   se pueden ajustar si se quiere, por ejemplo la cantidad de resultados por búsqueda o
   los tiempos de espera).

## Ejecución

```
python main.py
```

Al correrlo:

1. Pide por consola los productos a buscar, separados por coma (ej. `lapiz, vaso`). Si
   no se escribe nada válido, vuelve a preguntar.
2. Se abre una ventana de Chrome y empieza a buscar cada término en Mercado Libre,
   mostrando el avance en consola (`Procesando 1/2: buscando "lapiz"...`).
3. Si aparece un recaptcha, la consola lo indica y espera a que se resuelva
   manualmente antes de seguir.
4. Al terminar todas las búsquedas, guarda el Excel y espera un Enter en consola antes
   de cerrar Chrome.

### Advertencia sobre Mercado Libre

Mercado Libre puede pedir una verificación de cuenta o de seguridad (por ejemplo,
"Ingresa a tu cuenta" o validar identidad) en medio de la ejecución, especialmente si se
corren varias búsquedas seguidas. Esto es un control propio de la plataforma, no un
error del script. Si aparece:

- Resuélvelo manualmente en la ventana de Chrome que se abrió.
- Si no se resuelve a tiempo, el script reintenta una vez esa búsqueda y, si sigue
  fallando, continúa con el siguiente término en vez de detenerse (el intento fallido
  queda registrado en `logs/proceso.log`).

## Estructura del proyecto

```
main.py                     punto de entrada: genera las búsquedas y corre el proceso
services/
  generador_busquedas.py    pide los términos por consola y crea productos_busqueda.json
  buscador_selenium.py      abre Chrome y busca cada término en Mercado Libre
  extractor_resultados.py   extrae los datos de los primeros 5 resultados
  exportador_excel.py       consolida los resultados y los guarda en Excel
utils/
  config.py                 rutas, URL y valores configurables del proyecto
  logger.py                 escribe advertencias y errores en logs/proceso.log
  impresor.py               mensajes y progreso que se muestran en consola
output/                     ahí se guarda el Excel final (se crea al correr el script)
logs/                       ahí se guarda el log de errores (se crea al correr el script)
```

## Extras implementados

Además de lo pedido en el enunciado, el proyecto incluye estos puntos adicionales:

- **Config**: centraliza rutas, URL de Mercado Libre y valores configurables (cantidad
  de resultados, tiempos de espera, pausa entre búsquedas), leídos desde `.env`.
- **Logger**: registra advertencias y errores en `logs/proceso.log` (campos que no se
  encontraron, búsquedas fallidas, etc.), sin detener el proceso.
- **Impresor**: centraliza los mensajes que se muestran en consola, incluyendo el
  progreso de la búsqueda (`Procesando X/Y...`).
- **Manejo de errores y reintentos**: si una búsqueda falla (timeout, verificación de
  cuenta), se reintenta una vez antes de continuar con el siguiente término.

## Salidas generadas

- `output/resultados_busqueda.xlsx`: Excel con todos los resultados de todas las
  búsquedas, con las columnas término buscado, producto, precio, vendedor, calificación,
  envío gratis y link.
- `logs/proceso.log`: registro de advertencias (campos no encontrados en un resultado
  puntual) y errores (búsquedas que fallaron incluso tras el reintento).

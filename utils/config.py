import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    # nombres fijos de archivos/carpetas del proyecto
    NOMBRE_ARCHIVO_JSON = "productos_busqueda.json"
    NOMBRE_CARPETA_PERFIL = "chrome_profile"
    NOMBRE_CARPETA_OUTPUT = "output"
    NOMBRE_ARCHIVO_EXCEL = "resultados_busqueda.xlsx"
    NOMBRE_CARPETA_LOGS = "logs"
    NOMBRE_ARCHIVO_LOG = "proceso.log"

    # configurables por .env, con valor por defecto si no existe
    URL_MERCADOLIBRE = os.getenv("URL_MERCADOLIBRE", "https://www.mercadolibre.com.co")
    CANTIDAD_RESULTADOS = int(os.getenv("CANTIDAD_RESULTADOS", "5"))
    TIMEOUT_CORTO = int(os.getenv("TIMEOUT_CORTO", "10"))
    TIMEOUT_LARGO = int(os.getenv("TIMEOUT_LARGO", "30"))

    @staticmethod
    def raiz_proyecto():
        # utils/ está un nivel por debajo de la raíz del proyecto
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @classmethod
    def ruta_json_busquedas(cls):
        return os.path.join(cls.raiz_proyecto(), cls.NOMBRE_ARCHIVO_JSON)

    @classmethod
    def ruta_carpeta_perfil(cls):
        return os.path.join(cls.raiz_proyecto(), cls.NOMBRE_CARPETA_PERFIL)

    @classmethod
    def ruta_carpeta_output(cls):
        return os.path.join(cls.raiz_proyecto(), cls.NOMBRE_CARPETA_OUTPUT)

    @classmethod
    def ruta_excel(cls):
        return os.path.join(cls.ruta_carpeta_output(), cls.NOMBRE_ARCHIVO_EXCEL)

    @classmethod
    def ruta_carpeta_logs(cls):
        return os.path.join(cls.raiz_proyecto(), cls.NOMBRE_CARPETA_LOGS)

    @classmethod
    def ruta_log(cls):
        return os.path.join(cls.ruta_carpeta_logs(), cls.NOMBRE_ARCHIVO_LOG)

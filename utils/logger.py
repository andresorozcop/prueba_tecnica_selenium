import logging
import os

from utils.config import Config


class Logger:
    _logger = None

    @classmethod
    def _obtener_logger(cls):
        if cls._logger is not None:
            return cls._logger

        os.makedirs(Config.ruta_carpeta_logs(), exist_ok=True)

        logger = logging.getLogger("proceso")
        logger.setLevel(logging.INFO)

        # solo se escribe a archivo, la consola la maneja Impresor
        manejador = logging.FileHandler(Config.ruta_log(), encoding="utf-8")
        formato = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        manejador.setFormatter(formato)
        logger.addHandler(manejador)

        cls._logger = logger
        return logger

    @classmethod
    def advertencia(cls, mensaje):
        cls._obtener_logger().warning(mensaje)

    @classmethod
    def error(cls, mensaje):
        cls._obtener_logger().error(mensaje)

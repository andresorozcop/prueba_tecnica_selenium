class Impresor:
    @staticmethod
    def mostrar(mensaje):
        print(mensaje)

    @staticmethod
    def progreso(actual, total, texto=""):
        print(f"Procesando {actual}/{total}: {texto}")

    @staticmethod
    def aviso(mensaje):
        print(f"[AVISO] {mensaje}")

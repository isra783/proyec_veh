class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio

    # ----- MARCA -----
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, valor):
        self.__marca = valor

    # ----- MODELO -----
    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, valor):
        self.__modelo = valor

    # ----- AÑO -------
    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, valor):
        self.__anio = valor


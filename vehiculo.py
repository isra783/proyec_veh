class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año

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
    def año(self):
        return self.__año

    @año.setter
    def año(self, valor):
        self.__año = valor


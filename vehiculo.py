class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__encendido = False  # Inicializar el estado del vehículo

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

    # ----- ENCENDIDO -----
    @property
    def encendido(self):
        return self.__encendido

    # ====== MÉTODOS DE COMPORTAMIENTO ======
    def encender(self):
        if not self.__encendido:
            self.__encendido = True
            return "El vehículo ha sido encendido."
        return "El vehículo ya estaba encendido."

    def apagar(self):
        if self.__encendido:
            self.__encendido = False
            return "El vehículo ha sido apagado."
        return "El vehículo ya estaba apagado."

    # ====== MÉTODO STR ======
    def __str__(self):
        estado = "Encendido" if self.__encendido else "Apagado"
        return f"Vehículo: {self.__marca} {self.__modelo} ({self.__año}) - Estado: {estado}"


if __name__ == "__main__":
    # Crear un vehículo
    auto = Vehiculo("Toyota", "Corolla", 2023)

    # Ver estado inicial
    print(auto)
    print()
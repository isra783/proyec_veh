from motor import Motor
from vehiculo import Vehiculo


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindraje, motor):
        super().__init__(marca, modelo, año)
        self.__cilindraje = cilindraje  # En cc (centímetros cúbicos)
        self.__motor = motor  # Composición: la motocicleta "tiene un" motor
        self.__caballito_activo = False

    # ----- CILINDRAJE -----
    @property
    def cilindraje(self):
        return self.__cilindraje

    @cilindraje.setter
    def cilindraje(self, valor):
        self.__cilindraje = valor

    # ----- MOTOR -----
    @property
    def motor(self):
        return self.__motor

    # ====== MÉTODOS DE COMPORTAMIENTO ======
    def hacer_caballito(self):
        if self.encendido:
            if not self.__caballito_activo:
                self.__caballito_activo = True
                return "¡Woohoo! Haciendo caballito "
            return "Ya estás haciendo un caballito. ¡Ten cuidado!"
        return "No se puede hacer caballito. La motocicleta está apagada."

    def terminar_caballito(self):
        if self.__caballito_activo:
            self.__caballito_activo = False
            return "Has vuelto a las dos ruedas. Conducción segura."
        return "No estás haciendo ningún caballito."

    def usar_patada_arranque(self):
        if not self.encendido:
            # Simular que con la patada se enciende
            return self.encender() + " (usando patada de arranque)"
        return "La motocicleta ya está encendida. No necesitas la patada de arranque."

    # ====== MÉTODO STR (sobrescrito) ======
    def __str__(self):
        info_base = super().__str__()
        caballito = "Sí" if self.__caballito_activo else "No"
        return f"{info_base}\nCilindraje: {self.__cilindraje} cc | Caballito: {caballito}\n{self.__motor}"


if __name__ == "__main__":
    motor_moto = Motor("Gasolina", 2, 150)

    # Crear una motocicleta
    moto = Motocicleta("Yamaha", "YZF-R1", 2023, 998, motor_moto)

    print(moto)
    print()

    # Intentar hacer caballito con la moto apagada
    print(moto.hacer_caballito())
    print()

    # Usar patada de arranque
    print(moto.usar_patada_arranque())
    print()

    # Ahora sí hacer caballito
    print(moto.hacer_caballito())
    print()
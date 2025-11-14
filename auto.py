


from vehiculo import Vehiculo


class Motor:
    def __init__(self, tipo, cilindros, potencia):
        self.__tipo = tipo  # Ejemplo: "Gasolina", "Diesel", "Eléctrico"
        self.__cilindros = cilindros
        self.__potencia = potencia  # En HP (caballos de fuerza)

    @property
    def tipo(self):
        return self.__tipo

    @property
    def cilindros(self):
        return self.__cilindros

    @property
    def potencia(self):
        return self.__potencia

    def __str__(self):
        return f"Motor {self.__tipo} de {self.__cilindros} cilindros, {self.__potencia} HP"


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas, motor):
        super().__init__(marca, modelo, año)
        self.__numero_puertas = numero_puertas
        self.__motor = motor  # Composición: el automóvil "tiene un" motor
        self.__maletero_abierto = False

    # ----- NÚMERO DE PUERTAS -----
    @property
    def numero_puertas(self):
        return self.__numero_puertas

    @numero_puertas.setter
    def numero_puertas(self, valor):
        self.__numero_puertas = valor

    # ----- MOTOR -----
    @property
    def motor(self):
        return self.__motor

    # ====== MÉTODOS DE COMPORTAMIENTO ======
    def abrir_maletero(self):
        if not self.__maletero_abierto:
            self.__maletero_abierto = True
            return "El maletero ha sido abierto."
        return "El maletero ya estaba abierto."

    def cerrar_maletero(self):
        if self.__maletero_abierto:
            self.__maletero_abierto = False
            return "El maletero ha sido cerrado."
        return "El maletero ya estaba cerrado."

    def tocar_claxon(self):
        if self.encendido:
            return "¡BEEP BEEP!"
        return "No se puede tocar el claxon. El vehículo está apagado."

    # ====== MÉTODO STR (sobrescrito) ======
    def __str__(self):
        info_base = super().__str__()
        maletero = "Abierto" if self.__maletero_abierto else "Cerrado"
        return f"{info_base}\nPuertas: {self.__numero_puertas} | Maletero: {maletero}\n{self.__motor}"


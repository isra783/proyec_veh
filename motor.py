class Motor:
    def __init__(self, tipo, cilindros, potencia):
        self.__tipo = tipo
        self.__cilindros = cilindros
        self.__potencia = potencia
        self.__motor_encendido = False

    # ----- TIPO -----
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor

    # ----- CILINDROS -----
    @property
    def cilindros(self):
        return self.__cilindros

    @cilindros.setter
    def cilindros(self, valor):
        self.__cilindros = valor

    # ----- POTENCIA -----
    @property
    def potencia(self):
        return self.__potencia

    @potencia.setter
    def potencia(self, valor):
        self.__potencia = valor

    # ----- MOTOR ENCENDIDO -----
    @property
    def motor_encendido(self):
        return self.__motor_encendido

    # ====== MÉTODOS DE COMPORTAMIENTO ======
    def encender_motor(self):
        if not self.__motor_encendido:
            self.__motor_encendido = True
            return f"Motor {self.__tipo} encendido. ¡Vroom vroom!"
        return "El motor ya estaba encendido."

    def detener_motor(self):
        if self.__motor_encendido:
            self.__motor_encendido = False
            return "Motor detenido."
        return "El motor ya estaba detenido."

    def acelerar(self):
        if self.__motor_encendido:
            return f"Acelerando... {self.__potencia} HP en acción! 💨"
        return "No se puede acelerar. El motor está detenido."

    # ====== MÉTODO STR ======
    def __str__(self):
        estado_motor = "Encendido" if self.__motor_encendido else "Detenido"
        return f"Motor {self.__tipo} de {self.__cilindros} cilindros, {self.__potencia} HP - Estado: {estado_motor}"
import wpilib
import commands2
import phoenix5

class elev(commands2.Subsystem):
    def __init__(self):
        super().__init__()
        self.motor_esquerda = phoenix5.WPI_VictorSPX(8)
        self.motor_direita = phoenix5.WPI_VictorSPX(6)
        self.motores = wpilib.MotorControllerGroup(self.motor_esquerda, self.motor_direita)

    def motores_sentido_positivo(self):
        self.motores.set(1)

    def motores_sentido_negativo(self):
        self.motores.set(-1)
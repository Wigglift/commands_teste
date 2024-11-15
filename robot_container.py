import wpilib
import commands2
import comandos_elevacao
import commands2.button

class container_massa():
    def __init__(self) -> None:
        self.elevacao_of = comandos_elevacao
        self.controle = wpilib.Joystick(1)

    def elev_subir(self):
        commands2.button.joystickbutton(self.controle, 1).onTrue(commands2.cmd.run(lambda: self.elevacao_of.subir))

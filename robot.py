from robot_container import container_massa
import commands2

class MYR(commands2.TimedCommandRobot):
    def robotInit(self) -> None:
        self.Container = container_massa
    
    def teleopPeriodic(self) -> None:
        self.Container.elev_subir
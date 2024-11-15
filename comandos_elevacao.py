import commands2
from elevacao import elev

class subir(commands2.Command):
    def __init__(self, elevacao_herdado: elev):
        self.elevacao = elevacao_herdado

    def initialize(self):
        self.elevacao.motores_sentido_positivo()

    def isFinished(self):
        return True
    
class descer(commands2.Command):
    def __init__(self, elevacao_herdado: elev):
        self.elevacao = elevacao_herdado

    def initialize(self):
        self.elevacao.motores_sentido_negativo()

    def isFinished(self):
        return True

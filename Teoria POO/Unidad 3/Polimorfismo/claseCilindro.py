import math

from claseCuerpo import Cuerpo

class Cilindro(Cuerpo):
    __radio = 0.0

    def __init__(self, altura, radio):
        Cuerpo.__init__(self, altura)
        self.__radio = radio

    def __str__(self):
        cadena = 'Cilindro, altura = {}, radio = {}'.format(self.getAltura(), self.__radio)
        return cadena

    def superficieBase(self):
        return math.pi*self.__radio**2
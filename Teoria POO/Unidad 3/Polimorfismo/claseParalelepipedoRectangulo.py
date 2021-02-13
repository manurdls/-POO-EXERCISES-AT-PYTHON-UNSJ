import math

from claseCuerpo import Cuerpo

class ParalelepipedoRectangulo(Cuerpo):
    __lado1 = 0
    __lado2 = 0

    def __init__(self, altura, lado1, lado2):
        Cuerpo.__init__(self, altura)
        self.__lado1 = lado1
        self.__lado2 = lado2

    def __str__(self):
        cadena = 'Paralelepipedo Rectangulo, altura = {}, lado a= {}, lado b= {}'.format(self.getAltura(), self.__lado1, self.__lado2)
        return cadena

    def superficieBase(self):
        return self.__lado1*self.__lado2
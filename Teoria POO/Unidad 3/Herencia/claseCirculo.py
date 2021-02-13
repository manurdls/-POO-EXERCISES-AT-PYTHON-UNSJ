import math

class Circulo(object):
    __radio = 0.0

    def __init__(self, radio):
        self.__radio = radio

    def superficie(self):
        return math.pi*self.__radio**2

    def getRadio(self):
        return self.__radio

    def listar(self):
        print('Circulo')
        print('Radio: {0:3.2f}, superficie: {1:7.5f}'.format(self.__radio, self.superficie()))
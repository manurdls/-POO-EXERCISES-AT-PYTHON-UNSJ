import numpy as np

from claseCuerpo import Cuerpo

class Arreglo(object):
    __dimension = 0
    __actual = 0
    __cuerpos = None

    def __init__(self, dimension=10):
        self.__cuerpos = np.empty(dimension, dtype=Cuerpo)
        self.__dimension = dimension
        self.__cantidad = 0

    def agregarCuerpo(self, unCuerpo):
        self.__cuerpos[self.__actual] = unCuerpo
        self.__actual += 1

    def calcularVolumenCuerpos(self):
        for i in range(self.__actual):
            cuerpo = self.__cuerpos[i]
            print(str(cuerpo)+', Volumen = {0:7.2f}'.format(cuerpo.volumen()))
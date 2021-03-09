import numpy as np
from clasePunto import Punto

class arregloNumPy:
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    def __init__(self, dimension, incremento=5):
        self.__puntos = np.empty(dimension, dtype=Punto)
        self.__cantidad = 0
        self.__dimension = dimension
    def agregarPunto(self, unPunto):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__puntos.resize(self.__dimension)
        self.__puntos[self.__cantidad] = unPunto
        self.__cantidad += 1
    def getUnPunto(self, indice):
        return self.__puntos[indice]
    def mostrarPuntos(self):
        for i in range(self.__cantidad):
            self.__puntos[i].mostrarDatos()
    def calcularDistanciasP0(self, unPunto):
        for i in range(self.__cantidad):
            distancia = unPunto.distanciaEuclidea(self.__puntos[i])
            print('Distancia del punto {} al punto {} es {}'.format(unPunto, self.__puntos[i], distancia))
    def testArregloPuntos(self):
        p1 = Punto(4,5)
        p2 = Punto(3,4)
        p3 = Punto(-9,5)
        p4 = Punto(3,2)
        p5 = Punto(1,7)
        self.agregarPunto(p1)
        self.agregarPunto(p2)
        self.agregarPunto(p3)
        self.agregarPunto(p4)
        self.agregarPunto(p5)


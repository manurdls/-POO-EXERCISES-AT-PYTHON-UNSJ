from math import sqrt

class Punto:
    __x = -1
    __y = 0
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    def __str__(self):
        return '({},{}).'.format(self.__x, self.__y)
    def setX(self, v):
        self.__x = v
    def getX(self):
        return self.__x
    def setY(self, v):
        self.__y = v
    def getY(self):
        return self.__y
    def mostrarDatos(self):
        print("(x,y) = ({},{})".format(self.__x,self.__y))
    def mover(self, x, y):
        self.setX(x)
        self.setY(y)
    def distanciaEuclidea(self, otroPunto):
        distancia = sqrt((otroPunto.__x-self.__x)**2+(otroPunto.__y-self.__y)**2)
        return distancia
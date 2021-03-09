from clasePunto import Punto

class Lista:
    __puntos = []
    def __init__(self):
        self.__puntos = []
    def agregarPuntos(self, unPunto):
        self.__puntos.append(unPunto)
    def mostrarPuntos(self):
        for punto in self.__puntos:
            punto.mostrarDatos()
    def testListaPuntos(self):
        p1 = Punto(4,5)
        p2 = Punto(3,4)
        p3 = Punto(-9,5)
        p4 = Punto(3,2)
        p5 = Punto(1,7)
        self.agregarPuntos(p1)
        self.agregarPuntos(p2)
        self.agregarPuntos(p3)
        self.agregarPuntos(p4)
        self.agregarPuntos(p5)
    def getUnPunto(self, indice):
        return self.__puntos[indice]
    def calcularDistanciasP0(self, unPunto):
        for i in range(len(self.__puntos)):
            distancia = unPunto.distanciaEuclidea(self.__puntos[i])
            print("Distancia del punto {} al punto {} es {}".format(unPunto, self.__puntos[i], distancia))
class Manejador(object):
    __puntos = []

    def __init__(self):
        self.__puntos = []

    def agregarPunto(self, unPunto):
        self.__puntos.append(unPunto)

    def mostrarDatos(self):
        for i in self.__puntos:
            print(i)

    def toJSON(self):
        d = dict(
            __clas__ = self.__class__.__name__,
            puntos = [punto.toJSON() for punto in self.__puntos]
        )
        return d

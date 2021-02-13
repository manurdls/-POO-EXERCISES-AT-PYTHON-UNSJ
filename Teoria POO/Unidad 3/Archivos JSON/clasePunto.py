class Punto(object):
    __x = 0
    __y = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        cadena = '(x,y)=({},{})'.format(self.__x, self.__y)
        return cadena

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                x = self.__x,
                y = self.__y
            )
        )
        return d
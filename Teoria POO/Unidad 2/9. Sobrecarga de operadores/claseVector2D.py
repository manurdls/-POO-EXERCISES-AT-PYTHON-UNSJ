
class Vector2D:
    __x = 0.0
    __y = 0.0
    def __init__(self, x=-1, y=-1):
        self.__x = x
        self.__y = y
    def __str__(self):
        return '<x,y>=<{},{}>'.format(self.__x, self.__y)
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def __add__(self, otroVector):
        return Vector2D(self.__x+otroVector.getX(), self.__y+otroVector.getY())
    def __sub__(self, otroVector):
        return Vector2D(self.__x-otroVector.getX(), self.__y-otroVector.getY())
    def __mul__(self, escalar):
        print('Entro por sobrecarga normal')
        return Vector2D(self.__x*escalar, self.__y*escalar)
    def __rmul__(self, escalar):
        print('Entro por sobrecarga por derecha')
        return Vector2D(self.__x*escalar, self.__y*escalar)
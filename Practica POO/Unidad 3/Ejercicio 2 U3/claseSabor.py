class Sabor(object):
    __numero = 0
    __nombre = ''
    __descripcion = ''

    def __init__(self, num, nom, des):
        self.__numero = num
        self.__nombre = nom
        self.__descripcion = des

    def __str__(self):
        return 'Numero: %s, Nombre: %s, Descripcion: %s' % (self.__numero, self.__nombre, self.__descripcion)

    def getNombre(self):
        return self.__nombre

    def getNumero(self):
        return self.__numero
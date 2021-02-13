from claseEmpleado import Empleado

class Nodo(object):
    __empleado = None
    __siguiente = None

    def __init__(self, empleado):
        self.__empleado = empleado
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getEmpleado(self):
        return self.__empleado


class Empleado(object):
    __apellido = ""
    __nombre = ""
    __dependencia = ""
    __sueldoBasico = 0.0
    __antiguedad = 0
    __titulo = ""

    def __init__(self, apellido, nombre, dependencia, sueldoBasico, antiguedad, titulo):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__dependencia = dependencia
        self.__sueldoBasico = sueldoBasico
        self.__antiguedad = antiguedad
        self.__titulo = titulo

    def __str__(self):
        string = 'Nombre: {}\nApellido: {}\nDependencia: {}\nSueldo Básico: {}\n' \
                 'Antiguedad: {}\nTítulo: {}\n'.format(self.__apellido, self.__nombre, self.__dependencia, self.__sueldoBasico,
                                                     self.__antiguedad, self.__titulo)
        return string

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getDependencia(self):
        return self.__dependencia

    def getSueldoBasico(self):
        return self.__sueldoBasico

    def getAntiguedad(self):
        return self.__antiguedad

    def getTitulo(self):
        return self.__titulo

    def _reglaDeNegocio(self):
        pass

    def getSueldo(self):
        return self.getAntiguedad() + self._reglaDeNegocio()
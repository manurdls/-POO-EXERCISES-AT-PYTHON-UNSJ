
class Empleado(object):
    __nombre = ""
    __apellido = ""
    __sueldoBasico = 0.0
    __antiguedad = 0
    __turno = ""

    def __init__(self, nombre, apellido, sueldoBasico, antiguedad, turno):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__sueldoBasico = sueldoBasico
        self.__antiguedad = antiguedad
        self.__turno = turno

    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getSueldoBasico(self):
        return self.__sueldoBasico
    def getAntiguedad(self):
        return self.__antiguedad
    def getTurno(self):
        return self.__turno

    def getSueldo(self):
        sueldoBasico = self.getSueldoBasico()
        if self.getTurno() == "noche":
            sueldoBasico += 150

        return sueldoBasico + self.reglaDeNegocio()

    def reglaDeNegocio(self):
        pass
from claseEmpleado import Empleado
from claseTemporal import Temporal

class Externo(Temporal):
    __tarea = ''
    __montoViatico = 0
    __costoObra = 0
    __montoSeguroDeVida = 0

    def __init__(self, dni, nombre, direccion, telefono, fechaInicio, fechaFin, tarea, montoViatico, costoDeObra, montoSeguroDeVida):
        Temporal.__init__(self, dni, nombre, direccion, telefono, fechaInicio, fechaFin)
        self.__tarea = tarea
        self.__montoViatico = montoViatico
        self.__costoObra = costoDeObra
        self.__montoSeguroDeVida = montoSeguroDeVida

    def __str__(self):
        s = Empleado.__str__(self) + Temporal.__str__(self)
        s += 'Tarea: {}\nMonto viatico: {}\nCosto de la obra: {}' \
                   '\nMonto del seguro de vida: {}\nSueldo: {}\n'.format(self.__tarea,
                                                                         self.__montoViatico,
                                                                         self.__costoObra,
                                                                         self.__montoSeguroDeVida,
                                                                         Empleado.sueldo(self))
        return s

    def getTarea(self):
        return self.__tarea
    def getMontoViatico(self):
        return self.__montoViatico
    def getCostoObra(self):
        return self.__costoObra
    def getMontoSeguroDeVida(self):
        return self.__montoSeguroDeVida
    def getSueldo(self):
        return float(self.getCostoObra() - self.getMontoViatico() - self.getMontoSeguroDeVida())
    def setMontoViatico(self, nuevoViatico):
        self.__montoViatico = nuevoViatico
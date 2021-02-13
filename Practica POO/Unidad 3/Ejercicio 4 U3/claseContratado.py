from claseEmpleado import Empleado
from claseTemporal import Temporal

class Contratado(Temporal):
    valorPorHora = 100
    __cantidadHorasTrabajadas = 0

    def __init__(self, dni, nombre, direccion, telefono, fechaInicio, fechaFin, cantHoras):
        Temporal.__init__(self, dni, nombre, direccion, telefono, fechaInicio, fechaFin)
        self.__cantidadHorasTrabajadas = cantHoras

    def __str__(self):
        s = Empleado.__str__(self) +  Temporal.__str__(self)
        s += 'Cantidad de horas Trabajadas: {}\nSueldo: {}\n'.format(self.__cantidadHorasTrabajadas,
                                                                     Empleado.sueldo(self))
        return s

    @classmethod
    def modificarValorPorHora(cls, valor):
        if type(valor) == int:
            cls.valorPorHora = valor
        else:
            print('Error: se esperaba un valor de tipo entero.')

    @classmethod
    def getValorPorHora(cls):
        return cls.valorPorHora
    def getCantidadHorasTrabajadas(self):
        return self.__cantidadHorasTrabajadas
    def getSueldo(self):
        return float(self.getCantidadHorasTrabajadas() * self.getValorPorHora())
    def sumarHoras(self, horas):
        self.__cantidadHorasTrabajadas += horas
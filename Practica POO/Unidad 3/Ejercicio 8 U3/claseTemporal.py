import datetime
from claseEmpleado import Empleado

class Temporal(Empleado):
    __fechaInicio: datetime.date
    __fechaFin: datetime.date

    def __init__(self, dni, nombre, direccion, telefono, fechaInicio, fechaFin):
        Empleado.__init__(self, dni, nombre, direccion, telefono)
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin

    def __str__(self):
        s = 'Fecha de inicio: {}\nFecha de finalización: {}\n'.format(self.__fechaInicio,
                                                                      self.__fechaFin)
        return s

    def getFechaInicio(self):
        return self.__fechaInicio

    def getFechaFin(self):
        return self.__fechaFin
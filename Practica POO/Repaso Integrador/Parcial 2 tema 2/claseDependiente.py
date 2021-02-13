from claseEmpleado import Empleado

class Dependiente(Empleado):
    __especialidad = ""

    def __init__(self, nombre, apellido, sueldoBasico, antiguedad, turno, especialidad):
        super().__init__(nombre, apellido, sueldoBasico, antiguedad, turno)
        self.__especialidad = especialidad

    def getEspecialidad(self):
        return self.__especialidad

    def reglaDeNegocio(self):
        return 0
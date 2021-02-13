from claseEmpleado import Empleado

class Docente(Empleado):
    __cargo = ""
    __dedicacion = ""

    def __init__(self, apellido, nombre, dependencia, sueldoBasico, antiguedad, titulo, cargo, dedicacion):
        super().__init__(apellido, nombre, dependencia, sueldoBasico, antiguedad, titulo)
        self.__cargo = cargo
        self.__dedicacion = dedicacion

    def __str__(self):
        string = Empleado.__str__(self) + 'Cargo: {}\nDedicacion: {}\n'.format(self.__cargo, self.__dedicacion)
        return string

    def getCargo(self):
        return self.__cargo

    def getDedicacion(self):
        return self.__dedicacion

    def _reglaDeNegocio(self):
        retorna = self.getSueldoBasico()


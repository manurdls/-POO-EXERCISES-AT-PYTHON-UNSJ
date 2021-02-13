from claseEmpleado import Empleado

class Pau(Empleado):
    monotoHorasExtra = 0
    __area = ""
    __categoria = 0
    __horasExtra = 0

    def __init__(self, apellido, nombre, dependencia, sueldoBasico, antiguedad, titulo, area, categoria, horasExtra):
        super().__init__(apellido, nombre, dependencia, sueldoBasico, antiguedad, titulo)
        self.__area = area
        self.__categoria = categoria
        self.__horasExtra = horasExtra

    def __str__(self):
        string = Empleado.__str__(self) + 'Area: {}\nCategoría: {}\nHoras Extra: {}\n'.format(self.__area, self.__categoria, self.__horasExtra)
        return string

    def getArea(self):
        return self.__area

    def getCategoria(self):
        return self.__categoria

    def getHorasExtra(self):
        return self.__horasExtra
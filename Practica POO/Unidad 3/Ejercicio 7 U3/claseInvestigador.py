from clasePersona import Persona

class Investigador(Persona):
    __area = ''
    __tipo = ''

    def __init__(self, nombre, apellido, cuil, sueldoBasico, antiguedad, area, tipo):
        super().__init__(nombre, apellido, cuil, sueldoBasico, antiguedad)
        self.__area = area.title()
        self.__tipo = tipo.title()

    def __str__(self):
        s = super().__str__() + 'Area de investigación: {}\nTipo de investigación: {}\n'.format(
            self.__area, self.__tipo
        )
        if type(self) == Investigador:
            s += 'Sueldo: {}\n'.format(super().getSueldo())
        return s

    def getArea(self):
        return self.__area
    def getTipo(self):
        return self.__tipo

    def _getDiccionario(self):
        d = dict(
            area = self.__area,
            tipo = self.__tipo
        )
        return d
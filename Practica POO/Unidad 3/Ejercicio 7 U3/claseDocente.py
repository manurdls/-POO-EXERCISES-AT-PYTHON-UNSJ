from clasePersona import Persona

class Docente(Persona):
    __carrera = ''
    __catedra = ''
    __cargo = ''

    def __init__(self, nombre, apellido, cuil, sueldoBasico, antiguedad, carrera, catedra, cargo):
        if type(self) == Docente:
            super().__init__(nombre, apellido, cuil, sueldoBasico, antiguedad)
        self.__carrera = carrera.title()
        self.__catedra = catedra.title()
        self.__cargo = cargo.title()

    def __str__(self):
        s = super().__str__() + 'Carrera: {}\nCatedra: {}\nCargo: {}\n'.format(
            self.__carrera, self.__catedra, self.__cargo
        )
        if type(self) == Docente:
            s += 'Sueldo: {}\n'.format(super().getSueldo())
        return s

    def getCarrera(self):
        return self.__carrera
    def getCatedra(self):
        return self.__catedra
    def getCargo(self):
        return self.__cargo

    def _getExtraSueldo(self):
        extra = None
        if self.getCargo() == 'Simple':
            extra = super().getSueldoBasico()*0.1
        else:
            if self.getCargo() == 'Semiexclusivo':
                extra = super().getSueldoBasico()*0.2
            else:
                if self.getCargo() == 'Exclusivo':
                    extra = super().getSueldoBasico()*0.5
        return extra

    def _getDiccionario(self):
        d = dict(
            carrera = self.__carrera,
            catedra = self.__catedra,
            cargo = self.__cargo
        )
        return d
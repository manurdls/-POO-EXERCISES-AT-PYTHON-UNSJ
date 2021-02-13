from clasePersona import Persona

class PersonalDeApoyo(Persona):
    __categoria = 0

    def __init__(self, nombre, apellido, cuil, sueldoBasico, antiguedad, categoria):
        super().__init__(nombre, apellido, cuil, sueldoBasico, antiguedad)
        self.__categoria = int(categoria)

    def __str__(self):
        s = super().__str__() + 'Categoría: {}\nSueldo: {}\n'.format(self.__categoria, super().getSueldo())
        return s

    def getCategoria(self):
        return self.__categoria

    def _getExtraSueldo(self):
        extra = None
        if self.__categoria >= 1 and self.__categoria <= 10:
            extra = super().getSueldoBasico()*0.1
        else:
            if self.__categoria >= 11 and self.__categoria <= 20:
                extra = super().getSueldoBasico()*0.2
            else:
                if self.__categoria >= 21 and self.__categoria <= 22:
                    extra = super().getSueldoBasico()*0.3
        return extra

    def _getDiccionario(self):
        d = dict(
            categoria=self.__categoria
        )
        return d
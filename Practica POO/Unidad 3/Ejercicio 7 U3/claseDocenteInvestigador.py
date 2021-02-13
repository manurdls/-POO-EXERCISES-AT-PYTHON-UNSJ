from claseDocente import Docente
from claseInvestigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    __categoriaPrograma = 0
    __importeExtra = 0.0

    def __init__(self, nombre, apellido, cuil, sueldoBasico, antiguedad,
                 carrera, catedra, cargo,
                 area, tipo,
                 categoriaPrograma, importeExtra
                 ):
        Docente.__init__(self, nombre, apellido, cuil, sueldoBasico, antiguedad, carrera, catedra, cargo)
        Investigador.__init__(self, nombre, apellido, cuil, sueldoBasico, antiguedad, area, tipo)
        self.__categoriaPrograma = categoriaPrograma.upper()
        self.__importeExtra = float(importeExtra)

    def __str__(self):
        s = super().__str__() + 'Categoria en el programa de incentivos: {}\n' \
                                'Importe extra por docencia e investigación: {}\n' \
                                'Sueldo: {}\n'.format(
            self.__categoriaPrograma, self.__importeExtra, super().getSueldo()
        )
        return s

    def getCategoriaPrograma(self):
        return self.__categoriaPrograma

    def getImporteExtra(self):
        return self.__importeExtra

    def _getExtraSueldo(self):
        extra = super()._getExtraSueldo() + self.__importeExtra
        return extra

    def _getDiccionario(self):
        d1 = Docente._getDiccionario(self)
        d2 = Investigador._getDiccionario(self)
        d3 = dict(
            categoriaPrograma=self.__categoriaPrograma,
            importeExtra=self.__importeExtra
        )
        d1.update(d2)
        d1.update(d3)
        return d1
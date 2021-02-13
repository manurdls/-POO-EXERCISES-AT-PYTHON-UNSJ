from clasePersona import Persona
from claseDocente import Docente
from claseAlumno import Alumno

class Ayudante(Docente, Alumno):
    __concepto = ''
    __horasLIA = 0

    def __init__(self, dni, apellido, nombre, fechaIngreso, promedio, carrera, codigoCargo, agrupamiento, catedra, sueldo, concepto, horasLIA=0):
        #Docente.__init__(self, dni, apellido, nombre, codigoCargo, agrupamiento, catedra, sueldo)
        #Alumno.__init__(self, dni, apellido, nombre, fechaIngreso, promedio, carrera)
        super().__init__(dni, apellido, nombre, fechaIngreso, promedio, carrera, codigoCargo, agrupamiento, catedra, sueldo)
        self.__concepto = concepto
        self.__horasLIA = horasLIA

    def mostrarDatos(self):
        super().mostrarDatos()
        print('Datos Ayudante')
        print('Horas LIA {}'.format(self.__horasLIA))
        print('Concepto: {}'.format(self.__concepto))
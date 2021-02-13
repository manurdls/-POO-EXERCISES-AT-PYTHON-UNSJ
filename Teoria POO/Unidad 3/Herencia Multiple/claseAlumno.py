from clasePersona import Persona

class Alumno(Persona):
    __fechaIngreso = ''
    __promedio = 0.0
    __carrera = ''

    def __init__(self, dni, apellido, nombre, fechaIngreso, promedio, carrera, codigoCargo, agrupamiento, catedra, sueldo):
        super().__init__(dni, apellido, nombre, fechaIngreso, promedio, carrera, codigoCargo, agrupamiento, catedra, sueldo)
        self.__fechaIngreso = fechaIngreso
        self.__promedio = promedio
        self.__carrera = carrera

    def mostrarDatos(self):
        super().mostrarDatos()  #se ejecuta al mismo tiempo que super.mostrarDatos() de claseDocente
        print('Datos del Alumno')
        print('Carrera: {}, Fecha de ingreso: {}'.format(self.__carrera, self.__fechaIngreso))
        print('Promedio: {0}'.format(self.__promedio))
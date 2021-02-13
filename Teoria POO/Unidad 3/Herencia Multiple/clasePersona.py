class Persona(object):
    __dni = 0
    __apellido = ''
    __nombre = ''

    def __init__(self, dni, apellido, nombre, codigoCargo=0, agrupamiento=0 , catedra='', sueldo=0.0, fechaIngreso='', promedio='',carrera=''):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre

    def mostrarDatos(self):
        print('Datos Persona')
        print('DNI: {0:9d}'.format(self.__dni))
        print('Apellido: {}, Nombre: {}'.format(self.__apellido, self.__nombre))
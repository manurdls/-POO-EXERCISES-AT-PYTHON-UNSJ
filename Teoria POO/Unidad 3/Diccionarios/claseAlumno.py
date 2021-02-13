class Alumno(object):
    __registro = 0
    __nombre = ''
    __apellido = ''
    __carrera = ''

    def __init__(self, registro, nombre, apellido, carrera):
        self.__registro = registro
        self.__nombre = nombre
        self.__apellido = apellido
        self.__carrera = carrera

    def __str__(self):
        cadena = 'Registro: {},Carrera: {}\n'.format(self.__registro, self.__carrera)
        cadena += 'Apellido: {},Nombre: {}\n'.format(self.__apellido, self.__nombre)
        return cadena
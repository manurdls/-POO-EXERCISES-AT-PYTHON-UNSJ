class Persona:
    __dni = 0
    __apellido = ''
    __nombre = ''

    def __init__(self, dni, nombre, apellido):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido

    def __str__(self):
        cadena = 'DNI: ' + str(self.__dni) + '\n'
        cadena += 'Apellido: ' + self.__apellido + ', Nombre: ' + self.__nombre + '\n'
        return cadena
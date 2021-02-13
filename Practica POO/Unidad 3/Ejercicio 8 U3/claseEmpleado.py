class Empleado(object):
    __dni = ''
    __nombre = ''
    __direccion = ''
    __telefono = ''

    def __init__(self, dni, nombre, direccion, telefono):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    def __str__(self):
        return 'DNI: {}\nNombre: {}\nDireccion: {}\nTelefono: {}\n'.format(self.__dni,
                                                                           self.__nombre,
                                                                           self.__direccion,
                                                                           self.__telefono)

    def getDni(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    def getSueldo(self):
        pass
    def sueldo(self):
        return self.getSueldo()
    def sumarHoras(self, horas):
        pass
    def setSueldoBasico(self, nuevoBasico):
        pass
    def setMontoViatico(self, nuevoViatico):
        pass
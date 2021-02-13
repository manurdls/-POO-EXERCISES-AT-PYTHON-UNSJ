class tallerCapacitacion(object):
    __idTaller = 0
    __nombre = ''
    __vacantes = 0
    __montoInscripcion = 0

    def __init__(self, id, nombre, vacantes, monto):
        self.__idTaller = id
        self.__nombre = nombre
        self.__vacantes = vacantes
        self.__montoInscripcion = monto

    def __str__(self):
        return self.__nombre

    def getMontoInscripcion(self):
        return self.__montoInscripcion

    def getNombre(self):
        return self.__nombre

    def getId(self):
        return self.__idTaller

    def getVacantes(self):
        return self.__vacantes

    def ocuparVacante(self):
        self.__vacantes -= 1
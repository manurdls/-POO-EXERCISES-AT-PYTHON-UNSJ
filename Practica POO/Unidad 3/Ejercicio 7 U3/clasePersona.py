class Persona(object):
    __nombre = ''
    __apellido = ''
    __cuil = 0
    __sueldoBasico = 0.0
    __antiguedad = 0

    def __init__(self, nombre, apellido, cuil, sueldoBasico, antiguedad):
        self.__nombre = nombre.title()
        self.__apellido = apellido.title()
        self.__cuil = int(cuil)
        self.__sueldoBasico = float(sueldoBasico)
        self.__antiguedad = int(antiguedad)

    def __str__(self):
        s = 'Nombre: {}\nApellido: {}\nCuil: {}\nSueldo Basico: {}\nAntiguedad: {}\n'.format(
            self.__nombre, self.__apellido, self.__cuil, self.__sueldoBasico, self.__antiguedad
        )
        return s

    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getCuil(self):
        return self.__cuil
    def getSueldoBasico(self):
        return self.__sueldoBasico
    def getAntiguedad(self):
        return self.__antiguedad
    def _getExtraSueldo(self):
        pass
    def getSueldo(self):
        sueldo = self.getSueldoBasico() + (self.getSueldoBasico() * (self.__antiguedad/100))
        extra = self._getExtraSueldo()
        if extra != None:
            sueldo += extra
        return sueldo

    def _getDiccionario(self):
        pass

    def toJSON(self):
        atributos = dict(
            nombre=self.__nombre,
            apellido=self.__apellido,
            cuil=self.__cuil,
            sueldoBasico=self.__sueldoBasico,
            antiguedad=self.__antiguedad
        )
        atributos.update(self._getDiccionario())
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=atributos
        )
        return d
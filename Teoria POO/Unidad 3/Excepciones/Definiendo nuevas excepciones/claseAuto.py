from claseErrorAuto import ErrorAuto

class Auto(object):
    __marca : str
    __modelo : str
    __cilindradas : float
    __anio : int
    __velocidad = 0
    __color = ''
    __dominio : str
    __on = False

    def __init__(self, marca, modelo, cilindradas, anio, dominio, color = None):
        self.__marca = marca
        self.__modelo = modelo
        self.__cilindradas = cilindradas
        self.__anio = anio
        self.__dominio = dominio
        self.__color = color

    def __str__(self):
        cadena = 'Auto\n'
        cadena += 'Marca {}, modelo {}\n'.format(self.__marca, self.__modelo)
        cadena += 'Cilindradas: {}\n'.format(self.__cilindradas)
        cadena += 'Dominio: {}\n'.format(self.__dominio)
        cadena += 'Año de fabricacion: {}, color {}'.format(self.__anio, self.__color)
        return cadena

    def arrancar(self):
        if self.__on == False:
            self.__velocidad = 10
            self.__on = True
        else:
            raise ErrorAuto(self, 'Auto ya arrancado')    #################

    def acelerar(self):
        self.__velocidad += 10

    def getVelocidad(self):
        return self.__velocidad
    def getColor(self):
        return self.__color
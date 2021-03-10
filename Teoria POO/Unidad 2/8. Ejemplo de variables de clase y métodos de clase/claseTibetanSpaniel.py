
class TibetanSpaniel:
    #variables de clase
    nombreCientifico = 'Canis lupus familiaris'
    familia = 'Companion, herding'
    areaDeOrigen = 'Tibet'
    tasaDeAprendizaje = 9
    obediencia = 3
    resolucionDeProblemas = 8

    #variables de instancia
    __nombre: str
    __habilidad: int
    __jugueteFavorito: str

    def __init__(self, nombre, jugueteFavorito, habilidad):
        self.__nombre = nombre
        self.__habilidad = habilidad
        self.__jugueteFavorito = jugueteFavorito
    def __str__(self):
        return 'Nombre: %s, Habilidad: %d, Juguete Favorito: %s, ' \
               'Obediendica: %d' % (self.__nombre, self.__habilidad,
                                    self.__jugueteFavorito, self.getObediencia())

    #métodos de instancia
    def getNombre(self):
        return self.__nombre
    def getHabilidad(self):
        return self.__habilidad
    def getJugueteFavorito(self):
        return self.__jugueteFavorito

    #mátodos de clase
    @classmethod
    def getNombreCientifico(cls):
        return cls.nombreCientifico
    @classmethod
    def getFamilia(cls):
        return cls.familia
    @classmethod
    def getAreaDeOrigen(cls):
        return cls.areaDeOrigen
    @classmethod
    def getTasaDeAprendizaje(cls):
        return cls.tasaDeAprendizaje
    @classmethod
    def getObediencia(cls):
        return cls.obediencia
    @classmethod
    def getResolucionProblemas(cls):
        return cls.resolucionDeProblemas
    @classmethod
    def verRAza(cls):
        print('Características de la RAza')
        print('Nombre Científico: ' + cls.getNombreCientifico())
        print('Familia: ' + cls.getFamilia())
        print('Área de Origen: ' + cls.getAreaDeOrigen())
        print('Tasa de Aprendizaje: ' + str(cls.getTasaDeAprendizaje()))
        print('Obediencia: ' + str(cls.getObediencia()))
        print('Tasa de Resolución de problemas: ' + str(cls.getResolucionProblemas()))


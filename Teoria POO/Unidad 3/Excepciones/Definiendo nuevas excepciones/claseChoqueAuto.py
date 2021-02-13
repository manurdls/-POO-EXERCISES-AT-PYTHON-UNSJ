from claseErrorAuto import ErrorAuto

class ChoqueAuto(ErrorAuto):
    """Cuando se maneja demasiado rapido"""
    __velocidad = 0
    __otroAuto = None

    def __init__(self, auto, otroAuto, velocidad):
        super().__init__(auto, mensaje = 'ChoqueAuto: auto choco con %s a la velocidad de %d km/h' % (otroAuto, velocidad))
        self.__otroAuto = otroAuto
        self.__velocidad = velocidad

    def getOtroAuto(self):
        return self.__otroAuto
    def getVelocidad(self):
        return self.__velocidad
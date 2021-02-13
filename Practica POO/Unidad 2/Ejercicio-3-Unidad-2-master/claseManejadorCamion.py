from claseCamion import Camion

class manejadorCamion:
    __lista = []

    def __init__(self, idCa, nomCo, pat, marca, tara):
        self.__lista.append(Camion(idCa, nomCo, pat, marca, tara))

    def __str__(self):
        return 'Hay un total de {} camiones cargados'.format(self.getCantCamiones())

    def getCamion(self, id):
        return self.__lista[id-1]

    def getCantCamiones(self):
        n = 0
        for i in range(len(self.__lista)):
            n += 1
        return n

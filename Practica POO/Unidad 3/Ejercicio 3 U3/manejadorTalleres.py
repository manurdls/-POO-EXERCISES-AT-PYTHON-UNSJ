import numpy as np

from claseTallerCapacitacion import tallerCapacitacion

class manejadorTalleres(object):
    __talleres : np.array

    def __init__(self, dimension):
        self.__talleres = np.empty(dimension, dtype=tallerCapacitacion)

    def cargarTaller(self, taller):
        band = False
        i = 0
        while ((i < len(self.__talleres)) & (not band)):
            if type(self.__talleres[i]) == tallerCapacitacion: #no se puede poner if type(self.__talleres[i]) == None:
                hagocualquiercosa = 0
                del hagocualquiercosa
            else:
                self.__talleres[i] = tallerCapacitacion(int(taller[0]), taller[1], int(taller[2]), int(taller[3]))
                band = True
            i += 1

    def getListado(self):
        s = 'Listado de talleres:'
        for i in range(len(self.__talleres)):
            s += '\n' + str(i+1) + '. ' + self.__talleres[i].getNombre()
        return s

    def getCantidadTalleres(self):
        return len(self.__talleres)

    def modificarCupo(self, id):
        band = False
        if self.__talleres[id].getVacantes() > 0:
            band = True
            self.__talleres[id].ocuparVacante()
        return band

    def getTaller(self, id):
        return self.__talleres[id]

    def buscaTaller(self, idTaller):
        band = False
        i = 0
        while ((i < len(self.__talleres)) & (not band)):
            if self.__talleres[i].getId() == idTaller:
                band = True
            i += 1
        return band
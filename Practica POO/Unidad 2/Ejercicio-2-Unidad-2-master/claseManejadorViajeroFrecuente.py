from claseViajeroFrecuente import viajeroFrecuente
import copy

class manejadorViajeroFrecuente():
    __viajeros = []

    def addViajero(self, viajero):
        if isinstance(viajero, viajeroFrecuente):
            self.__viajeros.append(viajero)
        else:
            raise TypeError("Se esperaba una instancia de viajeroFrecuente")
        return True

    def buscarId(self, id):                 ##BUSCAR MEJOR SOLUCION
        ret = None
        i = 0
        flag = False
        while not flag and i < len(self.__viajeros):
            if self.__viajeros[i].getId() == id:
                flag = True
                ret = self.__viajeros[i]
            else:
                i += 1
        return ret

    def consultarMillas(self, viajero):
        print("Millas viajero pasado por parametro: {}".format(viajero.getMiles()))
        print("Millas viajero almacenado en la lista: {}".format(self.__viajeros[viajero.getId()-1].getMiles()))
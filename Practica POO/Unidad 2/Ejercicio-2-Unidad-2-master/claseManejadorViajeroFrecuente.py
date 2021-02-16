from claseViajeroFrecuente import viajeroFrecuente

class manejadorViajeroFrecuente():
    __viajeros = []

    def addViajero(self, viajero):
        if isinstance(viajero, viajeroFrecuente):
            self.__viajeros.append(viajero)
        else:
            raise TypeError("Se esperaba una instancia de viajeroFrecuente")
        return True
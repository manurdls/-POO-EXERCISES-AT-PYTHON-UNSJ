from claseViajeroFrecuente import viajeroFrecuente


class manejadorViajeroFrecuente:
    __lista = []

    def __init__(self):
        self.__lista = []

    def agregarViajero(self, viajero):
        if type(viajero) == viajeroFrecuente:
            self.__lista.append(viajero)
        else:
            print('Error: en esta lista solo se guardan datos de Viajeros Frecuentes')

    def mostrarLista(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])

    def buscarViajero(self, id):
        viajero = None
        for i in range(len(self.__lista)):
            if id == self.__lista[i].mostrarId():
                viajero = self.__lista[i]

        return viajero

import csv

from claseSabor import Sabor

class manejadorSabores(object):
    __sabores = []

    def __init__(self):
        __sabores = []

    def cargarDatos(self):
        archivo = open('sabores.csv')
        r = csv.reader(archivo, delimiter=',')
        for i in r:
            self.__sabores.append(Sabor(int(i[0]), i[1], i[2]))
        archivo.close()

    def getListado(self):
        s = ''
        for i in range(len(self.__sabores)):
            s += str(i+1) + '. ' + self.__sabores[i].getNombre() + '\n'
        return s

    def getCantSabores(self):
        return len(self.__sabores)

    def getSabor(self, codigo):
        band = False
        i = 0
        while ((i < len(self.__sabores)) & (not band)):
            #print('entro')
            if codigo == self.__sabores[i].getNumero():
                band = True
            else:
                i += 1
        return self.__sabores[i]

    def getNombre(self, i):
        return self.__sabores[i-1].getNombre()
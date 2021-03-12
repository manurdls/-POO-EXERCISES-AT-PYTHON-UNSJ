import csv
from claseCamion import Camion

class ManejadorCamiones(object):
    __camiones: list

    def __init__(self):
        self.__camiones = []

    def __str__(self):
        return self.__camiones

    def getCantCamiones(self):
        return len(self.__camiones)

    def getCamion(self, i):
        return self.__camiones[i]

    def cargarListaDesdeCSV(self, nomArchivo):
        archivo = open(nomArchivo)
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            self.__camiones.append(Camion(int(fila[0]),
                                          fila[1],
                                          fila[2],
                                          fila[3],
                                          float(fila[4])))
        archivo.close()
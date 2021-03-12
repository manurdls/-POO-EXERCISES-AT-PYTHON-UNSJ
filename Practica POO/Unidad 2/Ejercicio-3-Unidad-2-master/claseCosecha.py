import csv

from claseMatriz import Matriz

class Cosecha(object):
    __matriz: Matriz

    def __init__(self):
        self.__matriz = Matriz(20,45)

    def __str__(self):
        return self.__matriz

    def cargarCosechaDesdeCSV(self, nomArchivo):
        archivo = open(nomArchivo)
        reader = csv.reader(archivo, delimiter=',')
        ifila = 0
        for fila in reader:
            for i in range(len(fila)):
                self.__matriz.setCasillero(ifila,i,int(fila[i]))
            ifila += 1
        archivo.close()

    def getCantidadDeKilosDescargadosDeUnCamion(self, id):
        cosechaCamion = self.__matriz.getFila(id-1)
        cant = 0
        for i in range(len(cosechaCamion)):
            cant += cosechaCamion[i]
        return cant

    def getCantidadDeKilosDescargadosEnUnDia(self, dia):
        cosechaDia = self.__matriz.getColumna(dia-1)
        cant = 0
        for i in range(len(cosechaDia)):
            cant += cosechaDia[i]
        return cant

    def getCosechaEnUnDiaPorUnCamion(self, id, dia):
        return self.__matriz.getCasillero(id-1, dia-1)

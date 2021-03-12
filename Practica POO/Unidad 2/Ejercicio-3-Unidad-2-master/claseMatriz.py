

class Matriz(object):
    __datos = []

    def __init__(self, filas=10, columnas=5):
        for i in range(filas):
            self.__datos.append([])
            for j in range(columnas):
                self.__datos[i].append(0)

    def __str__(self):
        string = ''
        for fila in self.__datos:
            fi = ''
            for i in range(len(fila)):
                fi += str(fila[i]) + '  '
            string += fi + '\n'
        return string

    def setCasillero(self, fila, columna, dato):
        self.__datos[fila][columna] = dato

    def getCasillero(self, fila, columna):
        return self.__datos[fila][columna]

    def getFila(self, ifila):
        fila = []
        for i in range(len(self.__datos[ifila])):
            fila.append(self.__datos[ifila][i])
        return fila

    def getColumna(self, icolumna):
        columna = []
        for i in range(len(self.__datos)):
            columna.append(self.__datos[i][icolumna])
        return columna

# CÓDIGO PARA TESTEAR LA CLASE
'''
if __name__ == '__main__':
    matriz = Matriz()
    matriz.setCasillero(0,0,1)
    matriz.setCasillero(0,1,1)
    matriz.setCasillero(1, 2, 1)
    matriz.setCasillero(9,0,1)
    print(matriz)
    fila = matriz.getFila(0)
    print(fila)
    columna = matriz.getColumna(0)
    print(columna)
'''
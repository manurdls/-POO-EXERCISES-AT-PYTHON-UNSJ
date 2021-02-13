

class Cosecha:
    __matriz = []

    def __init__(self,reader):
        aux = []
        for fila in reader:
            aux.append(fila)

        self.__matriz = self.calcularTranspuesta(aux)
        self.__matriz = self.castAInt(self.__matriz)
        #print(type(self.__matriz[0][0]))

    def calcularTranspuesta(self, matriz):
        transpuesta = []
        for i in range(len(matriz[0])):
            transpuesta.append([])
            for j in range(len(matriz)):
                transpuesta[i].append(matriz[j][i])
        return transpuesta

    def castAInt(self,matriz):
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz[i][j] = int(matriz[i][j])
        return matriz

    def mostrarDatos(self):
        print(self.__matriz)

    def sumarDescarga(self, id, dia, peso, tara):
        self.__matriz[id-1][dia-1] = int(self.__matriz[id-1][dia-1]) + (peso - tara)
        #self.mostrarDatos()

    def getCosechaXCamion(self,idcamion):
        kilos = 0
        for i in range(len(self.__matriz[idcamion-1])):
            kilos += int(self.__matriz[idcamion-1][i])
        return kilos

    def getCosechaXDia(self,idcamion,dia):
        return self.__matriz[idcamion-1][dia-1]

    def generaArchivo(self,salida):
        aux = self.calcularTranspuesta(self.__matriz)
        for i in range(len(aux)):
            salida.writerow(aux[i])


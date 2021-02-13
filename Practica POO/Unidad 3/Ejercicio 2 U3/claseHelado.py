from claseSabor import Sabor


class Helado(object):
    __gramos = None
    __sabores = None

    def __init__(self, gramos, sabores):
        self.__gramos = gramos
        self.__sabores = []
        for i in sabores:
            self.agregarSabor(i)


    def __str__(self):
        s = ''
        for i in self.__sabores:
            s += '\n' + i.getNombre()
        return 'Gramos: ' + str(self.__gramos) + s

    def getGramos(self):
        return self.__gramos

    def agregarSabor(self, sabor):
        if type(sabor) == Sabor:
            self.__sabores.append(sabor)

    def getSabores(self):
        return self.__sabores

    def getNumSabores(self):
        numSabores = []
        for i in self.__sabores:
            numSabores.append(i.getNumero())
        return numSabores

    def getGramosDeUnSabor(self, num):
        gramos = 0.0
        cantSabores = len(self.__sabores)
        repeticiones = 0
        for i in self.__sabores:
            if num == i.getNumero():
                repeticiones += 1

        #print('Repeticiones: {}, Cantidad de sabores: {}'.format(repeticiones, cantSabores))
        if repeticiones != 0:
            if repeticiones == cantSabores:
                gramos = float(self.__gramos)
            else:
                if repeticiones == 1:
                    gramos = float(self.__gramos/cantSabores)
                else:
                    if repeticiones == 2:
                        gramos = float(self.__gramos/(cantSabores/2))
                    else:
                        if repeticiones == 3:
                            gramos = float(self.__gramos/cantSabores) + float(self.__gramos/(cantSabores/2))
        return gramos

    def buscaSaboresPorTipo(self, gramos, lista):
        if gramos == self.__gramos:
            for i in self.__sabores:
                band = False
                for j in lista:
                    if j == i.getNumero():
                        band = True
                if band == False:
                    lista.append(i.getNumero())
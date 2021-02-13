from claseHelado import Helado

from manejadorSabores import manejadorSabores

class manejadorHelados(object):
    __heladosVendidos = None

    def __init__(self):
        self.__heladosVendidos = []

    def agregarHelado(self, gramos, sabores):

        self.__heladosVendidos.append(Helado(gramos, sabores))

    def mostrarVendidos(self):
        print('Lista de helados vendidos: ')

        for i in range(len(self.__heladosVendidos)):
            print(str(i+1) + '. ' + str(self.__heladosVendidos[i]))

    def mostrarMasPedidos(self, sabores):
        lista = []
        cantSabores = sabores.getCantSabores()
        cont = 1
        for i in range(cantSabores):
            lista.append([])
            lista[i].append(0)
            lista[i].append(cont)
            cont += 1
        """for i in lista:
            print(i)"""

        for i in self.__heladosVendidos:
            numSabores = i.getNumSabores()
            for j in numSabores:
                band = False
                aux = 0
                while ((aux < len(lista)) & (not band)):
                    if j == lista[aux][1]:
                        lista[aux][0] += 1
                        band = True
                    aux += 1

        lista.sort(reverse=True)

        if lista[0][0] == 0:
            print('Aún no se realizaron ventas.')
        else:
            cont = 1
            i = 0
            while ((cont <= 5) & (i < len(lista))):
                if lista[i][0] != 0:
                    print('{}° mas pedidos:'.format(cont))
                    print('- ' + sabores.getNombre(lista[i][1]))

                actual = i
                sig = i+1
                band = False
                while ((sig < len(lista)) & (not band)):
                    if lista[actual][0] == lista[sig][0]:
                        if lista[sig][0] != 0:
                            print('- ' + sabores.getNombre(lista[sig][1]))
                        actual += 1
                        sig += 1
                    else:
                        band = True
                i = sig
                cont += 1

    def estimarGramosVendidos(self, num):
        gramosVendidos = 0.0
        for i in self.__heladosVendidos:
            gramosVendidos += i.getGramosDeUnSabor(num)
        return gramosVendidos

    def getNumSaboresPorTipo(self, gramos):
        lista = []
        for i in self.__heladosVendidos:
            i.buscaSaboresPorTipo(gramos, lista)

        for i in lista:
            print(i)

        return lista
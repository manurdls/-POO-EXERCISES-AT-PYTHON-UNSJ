class Conjunto:
    __lista = []

    def __init__(self, variable):
        self.__lista = []

        if type(variable) == list:
            self.__lista = variable.copy()
        else:
            for i in variable:
                for j in i:
                    self.__lista.append(int(j))
        #print(self.__lista)

    def mostrarConjunto(self):
        print(self.__lista)

    def __add__(self, conj2):

        aux = conj2.__lista.copy()

        for i in range(len(self.__lista)):
            for j in range(len(conj2.__lista)):
                if self.__lista[i] == conj2.__lista[j]:
                    aux.remove(conj2.__lista[j])

        return Conjunto(self.__lista + aux)

    def __sub__(self, conj2):

        aux = self.__lista.copy()

        for i in range(len(conj2.__lista)):
            for j in range(len(self.__lista)):
                if conj2.__lista[i] == self.__lista[j]:
                    aux.remove(self.__lista[j])

        return Conjunto(aux)

    def __eq__(self, conj2):
        band = True
        aux = self.__lista.copy()

        if len(aux) == len(conj2.__lista):
            aux.sort()
            conj2.__lista.sort()
            for i in range(len(aux)):
                if aux[i] != conj2.__lista[i]:
                    band = False
        else:
            band = False

        return band

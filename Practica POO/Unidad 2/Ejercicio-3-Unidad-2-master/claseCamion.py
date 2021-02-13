

class Camion:
    id = 0
    nomCond = ''
    patente = ''
    marca = ''
    tara = 0

    def __init__(self, id = 0, nomCond = '', patente = '', marca = '', tara = 0):
        self.__id = id
        self.__nomCond = nomCond
        self.__patente = patente
        self.__marca = marca
        self.__tara = tara

    def __str__(self):
        return 'Id: {}, Conductor: {}, Patente: {}, Marca: {}, Tara: {}'.format(self.__id,self.__nomCond,self.__patente,self.__marca,self.__tara)

    def getTara(self):
        return self.__tara

    def getPatente(self):
        return self.__patente

    def getConductor(self):
        return self.__nomCond

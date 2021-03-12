

class Camion(object):
    __id: int
    __nomCond: str
    __patente: str
    __marca: str
    __tara: float

    def __init__(self, id, nombCond, patente, marca, tara):
        self.__id = id
        self.__nomCond = nombCond
        self.__patente = patente
        self.__marca = marca
        self.__tara = tara

    def __str__(self):
        string = 'Id: {}\n' \
                 'Nombre Conductor: {}\n' \
                 'Patente: {}\n' \
                 'Marca: {}\n' \
                 'Tara: {}'.format(str(self.__id),
                                   self.__nomCond,
                                   self.__patente,
                                   self.__marca,
                                   str(self.__tara))
        return string

    def getPatente(self):
        return self.__patente
    def getConductor(self):
        return self.__nomCond
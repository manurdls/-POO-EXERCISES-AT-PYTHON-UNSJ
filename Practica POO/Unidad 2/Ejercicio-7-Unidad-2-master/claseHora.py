class Hora:
    __h = 0
    __m = 0
    __s = 0

    def __init__(self, h=0, m=0, s=0):
        if type(h) == list:
            self.__h = h[0]
            self.__m = h[1]
            self.__s = h[2]
        else:
            self.__h = h
            self.__m = m
            self.__s = s

    def __str__(self):
        return 'Hora: {}:{}:{}'.format(self.__h, self.__m, self.__s)

    def getH(self):
        return self.__h

    def getM(self):
        return self.__m

    def getS(self):
        return self.__s

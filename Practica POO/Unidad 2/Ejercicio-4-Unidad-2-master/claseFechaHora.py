class FechaHora:
    __d = 0
    __mes = 0
    __a = 0
    __s = 0
    __m = 0
    __h = 0
    __nDiasXMes = []

    def __init__(self, d=31, mes=12, a=2020, h=0, m=0, s=0):
        self.__d = d
        self.__mes = mes
        self.__a = a
        self.__s = s
        self.__m = m
        self.__h = h

        self.__nDiasXMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.verificarSiEsBisiesto(a) == True:
            self.__nDiasXMes[1] = 29     #febrero

        #print(self.__nDiasXMes)

    def mostrarCantDiasMeses(self):
        print(self.__nDiasXMes)

    def verificarSiEsBisiesto(self, a):
        band = False
        if a % 4 == 0:
            if a % 100 == 0:
                if a % 400 == 0:
                    band = True
            else:
                band = True
        return band

    def Mostrar(self):
        print('Fecha: {}/{}/{} , Hora: {}:{}:{}'.format(self.__d, self.__mes, self.__a, self.__h, self.__m, self.__s))

    def PonerEnHora(self, h=0, m=0, s=0):
        self.__h = h
        self.__m = m
        self.__s = s

    def AdelantarHora(self, h=0, m=0, s=0):

        auxH = self.__h + h
        auxM = self.__m + m
        auxS = self.__s + s

        if ((auxS >= 60) or (auxM >= 60) or (auxH >= 24)):
            if auxS >= 60:
                minutos = 0
                while auxS >= 60:
                    auxS -= 60
                    minutos += 1
                auxM += minutos
            self.__s = auxS

            if ((auxM >= 60) or (auxH >= 24)):
                if auxM >= 60:
                    horas = 0
                    while auxM >= 60:
                        auxM -= 60
                        horas += 1
                    auxH += horas
                self.__m = auxM

                if auxH >= 24:
                    dias = 0
                    while auxH >= 24:
                        auxH -= 24
                        dias +=1
                    self.aumentarDias(dias)
                self.__h = auxH
            else:
                self.__m = auxM
                self.__h = auxH
        else:
            self.__h = auxH
            self.__m = auxM
            self.__s = auxS

    def aumentarDias(self, dias):

        auxDias = self.__d + dias

        if auxDias > self.__nDiasXMes[self.__mes - 1]:
            indiceMes = self.__mes - 1
            while auxDias > self.__nDiasXMes[indiceMes]:
                auxDias -= self.__nDiasXMes[indiceMes]
                if indiceMes == 11:
                    indiceMes = 0
                    self.__a += 1
                    if self.verificarSiEsBisiesto(self.__a) == True:
                        self.__nDiasXMes[1] = 29
                    else:
                        self.__nDiasXMes[1] = 28
                else:
                    indiceMes += 1
            self.__d = auxDias
            self.__mes = indiceMes + 1
        else:
            self.__d = auxDias

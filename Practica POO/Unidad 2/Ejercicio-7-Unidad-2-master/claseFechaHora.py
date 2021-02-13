from claseHora import Hora

class FechaHora:
    __d = 0
    __mes = 0
    __a = 0
    __s = 0
    __m = 0
    __h = 0
    __nDiasXMes = []

    def __init__(self, d=1, mes=1, a=2020, h=0, m=0, s=0):
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

    def __str__(self):
        return 'Fecha: {}/{}/{} , Hora: {}:{}:{}'.format(self.__d, self.__mes, self.__a, self.__h, self.__m, self.__s)

    def getHora(self):
        return self.__h

    def getMinutos(self):
        return self.__m

    def getSegundos(self):
        return self.__s

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

    def PonerEnHora(self, h=0, m=0, s=0):
        self.__h = h
        self.__m = m
        self.__s = s


    def __add__(self, h):

        if type(h) == list:
            auxH = self.__h + h[0]
            auxM = self.__m + h[1]
            auxS = self.__s + h[2]
        else:
            if type(h) == FechaHora:
                auxH = self.__h + h.__h
                auxM = self.__m + h.__m
                auxS = self.__s + h.__s
            else:
                if type(h) == Hora:
                    auxH = self.__h + h.getH()
                    auxM = self.__m + h.getM()
                    auxS = self.__s + h.getS()
                else:
                    if type(h) == int:
                        auxH = self.__h + (24 * h)
                        auxM = self.__m
                        auxS = self.__s

        nD = self.__d
        nMes = self.__mes
        nA = self.__a
        nH = self.__h
        nM = self.__m
        nS = self.__s

        if ((auxS >= 60) or (auxM >= 60) or (auxH >= 24)):
            if auxS >= 60:
                minutos = 0
                while auxS >= 60:
                    auxS -= 60
                    minutos += 1
                auxM += minutos
            nS = auxS

            if ((auxM >= 60) or (auxH >= 24)):
                if auxM >= 60:
                    horas = 0
                    while auxM >= 60:
                        auxM -= 60
                        horas += 1
                    auxH += horas
                nM = auxM

                if auxH >= 24:
                    dias = 0
                    while auxH >= 24:
                        auxH -= 24
                        dias +=1
                    lista = self.aumentarDias(dias, nD, nMes, nA)
                    nD = lista[0]
                    nMes = lista[1]
                    nA = lista[2]
                nH = auxH
            else:
                nM = auxM
                nH = auxH
        else:
            nH = auxH
            nM = auxM
            nS = auxS
        return FechaHora(nD, nMes, nA, nH, nM, nS)

    def __radd__(self, h):

        if type(h) == list:
            auxH = self.__h + h[0]
            auxM = self.__m + h[1]
            auxS = self.__s + h[2]
        else:
            if type(h) == FechaHora:
                auxH = self.__h + h.__h
                auxM = self.__m + h.__m
                auxS = self.__s + h.__s
            else:
                if type(h) == Hora:
                    auxH = self.__h + h.getH()
                    auxM = self.__m + h.getM()
                    auxS = self.__s + h.getS()
                else:
                    if type(h) == int:
                        auxH = self.__h + (24 * h)
                        auxM = self.__m
                        auxS = self.__s
        nD = self.__d
        nMes = self.__mes
        nA = self.__a
        nH = self.__h
        nM = self.__m
        nS = self.__s

        if ((auxS >= 60) or (auxM >= 60) or (auxH >= 24)):
            if auxS >= 60:
                minutos = 0
                while auxS >= 60:
                    auxS -= 60
                    minutos += 1
                auxM += minutos
            nS = auxS

            if ((auxM >= 60) or (auxH >= 24)):
                if auxM >= 60:
                    horas = 0
                    while auxM >= 60:
                        auxM -= 60
                        horas += 1
                    auxH += horas
                nM = auxM

                if auxH >= 24:
                    dias = 0
                    while auxH >= 24:
                        auxH -= 24
                        dias +=1
                    lista = self.aumentarDias(dias, nD, nMes, nA)
                    nD = lista[0]
                    nMes = lista[1]
                    nA = lista[2]
                nH = auxH
            else:
                nM = auxM
                nH = auxH
        else:
            nH = auxH
            nM = auxM
            nS = auxS
        return FechaHora(nD, nMes, nA, nH, nM, nS)

    def aumentarDias(self, dias, dia, mes, anio):
        diasXMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.verificarSiEsBisiesto(anio):
            diasXMes[1] = 29

        auxDias = dia + dias

        if auxDias > diasXMes[mes - 1]:
            indiceMes = mes - 1
            while auxDias > diasXMes[indiceMes]:
                auxDias -= diasXMes[indiceMes]
                if indiceMes == 11:
                    indiceMes = 0
                    anio = anio + 1
                    if self.verificarSiEsBisiesto(anio) == True:
                        diasXMes[1] = 29
                    else:
                        diasXMes[1] = 28
                else:
                    indiceMes += 1
            dia = auxDias
            mes = indiceMes + 1
        else:
            dia = auxDias
        return [dia, mes, anio]




    def __sub__(self, hora):
        if type(hora) == list:
            auxH = self.__h - hora[0]
            auxM = self.__m - hora[1]
            auxS = self.__s - hora[2]
        else:
            if type(hora) == FechaHora:
                auxH = self.__h - hora.__h
                auxM = self.__m - hora.__m
                auxS = self.__s - hora.__s
            else:
                if type(hora) == int:
                    auxH = self.__h - 24 * hora
                    auxM = self.__m
                    auxS = self.__s
                else:
                    if type(hora) == Hora:
                        auxH = self.__h - hora.getH()
                        auxM = self.__m - hora.getM()
                        auxS = self.__s - hora.getS()

        nD = self.__d
        nMes = self.__mes
        nA = self.__a
        nH = self.__h
        nM = self.__m
        nS = self.__s

        if ((auxS < 0) or (auxM < 0) or (auxH < 24)):
            if auxS < 0:
                minutos = 0
                while auxS < 0:
                    auxS += 60
                    minutos += 1
                auxM -= minutos
            nS = auxS

            if ((auxM < 0) or (auxH < 0)):
                if auxM < 0:
                    horas = 0
                    while auxM < 0:
                        auxM += 60
                        horas += 1
                    auxH -= horas
                nM = auxM

                if auxH < 0:
                    dias = 0
                    while auxH < 0:
                        auxH += 24
                        dias +=1
                    lista = self.disminuirDias(dias, nD, nMes, nA)
                    nD = lista[0]
                    nMes = lista[1]
                    nA = lista[2]
                nH = auxH
            else:
                nM = auxM
                nH = auxH
        else:
            nH = auxH
            nM = auxM
            nS = auxS
        return FechaHora(nD, nMes, nA, nH, nM, nS)

    def disminuirDias(self, dias, dia, mes, anio):
        diasXMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.verificarSiEsBisiesto(anio):
            diasXMes[1] = 29

        auxDias = dia - dias
        indiceMes = mes - 1
        if auxDias <= 0:
            while auxDias <= 0:
                indiceMes -= 1
                if indiceMes == -1:
                    indiceMes = 11
                    anio = anio - 1
                    if self.verificarSiEsBisiesto(anio) == True:
                        diasXMes[1] = 29
                    else:
                        diasXMes[1] = 28
                auxDias += diasXMes[indiceMes]
            dia = auxDias
            mes = indiceMes + 1
        else:
            dia = auxDias
        return [dia, mes, anio]

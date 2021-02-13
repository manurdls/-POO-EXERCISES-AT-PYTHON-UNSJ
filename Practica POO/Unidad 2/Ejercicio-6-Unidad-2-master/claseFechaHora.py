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

    def aumentarDias(self, dias):

        auxDias = self.__d + dias

        if auxDias > self.__nDiasXMes[self.__mes - 1]:
            indiceMes = self.__mes - 1
            while auxDias > self.__nDiasXMes[indiceMes]:
                print(auxDias, self.__nDiasXMes[indiceMes])
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

    def __add__(self, hora):                                #hace practicamente lo mismo que el método adelantarHora
                                                            #del ejercicio 4 pero mucho más optimizado
        if type(hora) == list:
            auxH = self.__h + hora[0]
            auxM = self.__m + hora[1]
            auxS = self.__s + hora[2]
        else:
            if type(hora) == FechaHora:
                auxH = self.__h + hora.__h
                auxM = self.__m + hora.__m
                auxS = self.__s + hora.__s

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

    def __sub__(self, hora):                                #hace practicamente lo mismo que el método adelantarHora
                                                            #del ejercicio 4 pero mucho más optimizado
        if type(hora) == list:
            auxH = self.__h - hora[0]
            auxM = self.__m - hora[1]
            auxS = self.__s - hora[2]
        else:
            if type(hora) == FechaHora:
                auxH = self.__h - hora.__h
                auxM = self.__m - hora.__m
                auxS = self.__s - hora.__s

        if ((auxS < 0) or (auxM < 0) or (auxH < 24)):
            if auxS < 0:
                minutos = 0
                while auxS < 0:
                    auxS += 60
                    minutos += 1
                auxM -= minutos
            self.__s = auxS

            if ((auxM < 0) or (auxH < 0)):
                if auxM < 0:
                    horas = 0
                    while auxM < 0:
                        auxM += 60
                        horas += 1
                    auxH -= horas
                self.__m = auxM

                if auxH < 0:
                    dias = 0
                    while auxH < 0:
                        auxH += 24
                        dias +=1
                    self.disminuirDias(dias)
                self.__h = auxH
            else:
                self.__m = auxM
                self.__h = auxH
        else:
            self.__h = auxH
            self.__m = auxM
            self.__s = auxS

    def disminuirDias(self, dias):
        auxDias = self.__d - dias
        indiceMes = self.__mes - 1
        if auxDias <= 0:
            while auxDias <= 0:
                indiceMes -= 1
                if indiceMes == -1:
                    indiceMes = 11
                    self.__a -= 1
                    if self.verificarSiEsBisiesto(self.__a):
                        self.__nDiasXMes[1] = 29
                    else:
                        self.__nDiasXMes[1] = 28
                auxDias += self.__nDiasXMes[indiceMes]
            self.__d = auxDias
            self.__mes = indiceMes + 1
        else:
            self.__d = auxDias

    def __gt__(self, objeto):
        band = False
        if self.__a > objeto.__a:
            band = True
        else:
            if ((self.__a == objeto.__a) & (self.__mes > objeto.__mes)):
                band = True
            else:
                if ((self.__mes == objeto.__mes) & (self.__d > objeto.__d)):
                    band = True
                else:
                    if ((self.__d == objeto.__d) & (self.__h > objeto.__h)):
                        band = True
                    else:
                        if ((self.__h == objeto.__h) & (self.__m > objeto.__m)):
                            band = True
                        else:
                            if ((self.__m == objeto.__m) & (self.__s > objeto.__s)):
                                band = True
        return band


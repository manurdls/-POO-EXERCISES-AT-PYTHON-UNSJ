

class Menu():
    __switcher = None

    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.consultarMillas,
                            2:self.acumularMillas,
                            3:self.canjearMillas
                        }
    def getSwitcher(self):
        return self.__switcher

    def option(self, opt, viajero):
        func = self.__switcher.get(opt, lambda: print("Opcion no valida"))
        if opt == 0:
            func()
        else:
            func(viajero)

    def salir(self):
        print("Fin programa")

    def consultarMillas(self, viajero):
        print("Millas acumuladas: {}".format(viajero.getMiles()))

    def acumularMillas(self, viajero):
        miles = int(input("Ingrese las millas a acumular: "))
        viajero.acumularMiles(miles)

    def canjearMillas(self, viajero):
        miles = int(input("Ingrese las millas a canjear: "))
        viajero.canjearMiles(miles)
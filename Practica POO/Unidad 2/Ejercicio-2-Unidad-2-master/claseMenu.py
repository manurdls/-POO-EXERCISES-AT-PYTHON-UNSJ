

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

    def option(self, opt, manejaVF):
        func = self.__switcher.get(opt, lambda: print("Opcion no valida"))
        if opt == 0:
            func()
        else:
            func(manejaVF)

    def salir(self):
        print("Fin programa")

    def consultarMillas(self, manejaVF):
        print("consultar millas")

    def acumularMillas(self, manejaVF):
        print("acumular millas")

    def canjearMillas(self, manejaVF):
        print("canjear millas")
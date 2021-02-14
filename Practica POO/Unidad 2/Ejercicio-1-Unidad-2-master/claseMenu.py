class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.incisoA,
                            2:self.incisoB,
                            3:self.incisoC,
                         }
    def getSwitcher(self):
        return self.__switcher
    def option(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()
    def salir(self):
        print('Fin programa')
    def incisoA(self):
        print('incisoA')
    def incisoB(self):
        print('incisoB')
    def incisoC(self):
        print('incisoC')
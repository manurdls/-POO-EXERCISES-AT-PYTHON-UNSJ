class Menu:
    __switcher=None
    def _init_(self):
        self.__switcher = { 0:self.salir,
                            1:self.unionConjuntos,
                            2:self.diferenciaConjuntos,
                            3:self.igualdadConjuntos,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()
    def salir(self):
        print('Salir')
    def unionConjuntos(self):
        print('Unión')
    def diferenciaConjuntos(self):
        print('Diferencia')
    def igualdadConjuntos(self):
        print('Igualdad')





if _name_ == '_main_':
    menu=Menu()
    salir = False
    while not salir:
        print("""
              0 Salir
              1 Union de dos conjuntos
              2 Diferencia de dos conjuntos
              3 Igualdad entre dos conjuntos""")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op)
        salir = op == 0
from limpiarPantalla import limpiarPantalla
from interface import IInterface

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.insertarElemento,
                            2:self.agregarElemento,
                            3:self.mostrarElemento,
                            4:self.mostrarLista,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op, lista):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        if op >= 1 and op <= 4:
            func(lista)
        else:
            func()
    def salir(self):
        print('Chau...')

    def insertarElemento(self, lista):
        band = IInterface(lista).insertarElemento(self.__ingresarPosicion(), self.__ingresarElemento())
        if band:
            print('El elemento se ha insertado correctamente')

    def agregarElemento(self, lista):
        band = IInterface(lista).agregarElementoFin(self.__ingresarElemento())
        if band:
            print('El elemento se ha agregado correctamente')

    def mostrarElemento(self, lista):
        elemento = IInterface(lista).mostrarElemento(self.__ingresarPosicion())
        if elemento != None:
            print('Datos del elemento de tipo {}: {}'.format(type(elemento), elemento))

    def mostrarLista(self, lista):
        limpiarPantalla()
        print(lista)

    def __ingresarPosicion(self):
        band = False
        while not band:
            try:
                posicion = int(input('Ingrese la posicion: '))
                assert posicion >= 0, 'La posicion de una lista no puede ser negativa'
            except ValueError:
                limpiarPantalla()
                print('Error: habia que ingresar un entero')
            except:
                limpiarPantalla()
                print('Error: la posicion de una lista no puede ser negativa')
            else:
                band = True
                limpiarPantalla()
        return posicion

    def __ingresarElemento(self):
        band = False
        while not band:
            try:
                elemento = int(input('Ingrese un entero: '))
            except ValueError:
                limpiarPantalla()
                print('Error: habia que ingresar un entero')
            else:
                band = True
                limpiarPantalla()
        return elemento
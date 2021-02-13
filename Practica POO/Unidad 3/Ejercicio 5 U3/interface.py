from zope.interface import Interface

class IInterface(Interface):
    def insertarElemento(posicion, componente):
        pass

    def agregarElementoFin(componente):
        pass

    def mostrarElemento(posicion):
        pass
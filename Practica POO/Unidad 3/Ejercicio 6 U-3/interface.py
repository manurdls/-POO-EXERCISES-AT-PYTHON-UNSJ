from zope.interface import Interface

class IInterface(Interface):
    def insertarElemento(self, posicion, componente):
        pass

    def agregarElementoFin(self, componente):
        pass
from claseNodo import Nodo
from interface import IInterface
from zope.interface import implementer

@implementer(IInterface)
class Lista(object):
    __comienzo = None
    __tope=0

    def __init__(self):
        self.__comienzo = None

    def __str__(self):
        aux = self.__comienzo
        band = True
        s = '[ '
        while aux != None:
            if band:
                s = '[ {}'.format(str(aux.getDato()))
                band = False
            else:
                s += ', {}'.format(str(aux.getDato()))
            aux = aux.getSiguiente()
        s += ']'
        return s

    def agregarElementoInicio(self, componente):
        nuevoNodo = Nodo(componente)
        nuevoNodo.setSiguiente(self.__comienzo)
        self.__comienzo = nuevoNodo
        self.__tope += 1

    def agregarElementoFin(self, componente):
        retorno = False
        if self.__comienzo == None:
            self.agregarElementoInicio(componente)
            retorno = True
        else:
            aux = self.__comienzo
            siguiente = aux.getSiguiente()
            while siguiente != None:
                aux = siguiente
                siguiente = siguiente.getSiguiente()
            nuevoNodo = Nodo(componente)
            nuevoNodo.setSiguiente(None)
            aux.setSiguiente(nuevoNodo)
            self.__tope += 1
            retorno = True
        return retorno

    def insertarElemento(self, posicion, componente):
        retorno = False
        mensajeError = 'Error: posicion ingresada fuera de rango, la lista tiene {} componentes'.format(self.__tope)
        if posicion == 0:
            self.agregarElementoInicio(componente)
            retorno = True
        else:
            if self.__comienzo == None:
                print(mensajeError)
            else:
                i = 0
                aux = self.__comienzo
                while i < posicion and aux != None:
                    anterior = aux
                    aux = aux.getSiguiente()
                    i += 1
                try:
                    assert i == posicion and aux != None,'Error'
                except:
                    print(mensajeError)
                else:
                    nuevoNodo = Nodo(componente)
                    nuevoNodo.setSiguiente(aux)
                    anterior.setSiguiente(nuevoNodo)
                    self.__tope += 1
                    retorno = True
        return retorno

    def mostrarLista(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()

    def mostrarElemento(self, posicion):
        retorno = None
        if self.__comienzo == None:
            print('Error: la lista está vacia')
        else:
            try:
                assert posicion < self.__tope,'Error'
            except:
                print('Error: posicion ingresada fuera de rango, la lista tiene {} componentes'.format(self.__tope))
            else:
                aux = self.__comienzo
                i = 0
                while i < posicion and aux != None:
                    aux = aux.getSiguiente()
                    i += 1
                retorno = aux.getDato()
        return retorno
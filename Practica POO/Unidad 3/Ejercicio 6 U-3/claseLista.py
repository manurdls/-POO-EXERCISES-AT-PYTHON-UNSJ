from claseNodo import Nodo
from interface import IInterface
from zope.interface import implementer
from claseNuevo import Nuevo
from claseUsado import Usado

@implementer(IInterface)
class Lista(object):
    __comienzo = None
    __actual = None
    __indice = 0
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

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def __len__(self):
        return self.__tope

    def agregarElementoInicio(self, componente):
        nuevoNodo = Nodo(componente)
        nuevoNodo.setSiguiente(self.__comienzo)
        self.__comienzo = nuevoNodo
        self.__tope += 1
        self.__actual = nuevoNodo

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

    def obtenerElemento_xPosicion(self, posicion):
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

    def obtenerElemento_xPatente(self, patente):
        retorno = None
        if self.__comienzo == None:
            print('Error: la lista está vacia')
        else:
            band = False
            aux = self.__comienzo
            while not band and aux != None:
                siguiente = aux.getSiguiente()
                vehiculo = aux.getDato()
                if type(vehiculo) == Usado:
                    if patente == vehiculo.getPatente():
                        retorno = vehiculo
                        band = True
                aux = siguiente
        return retorno

    def obtenerVehiculoMasEconomico(self):
        vehiculo_mas_economico = None
        min = 999999999
        for vehiculo in self:
            importe_venta = vehiculo.getImporteVenta()
            if importe_venta < min:
                min = importe_venta
                vehiculo_mas_economico = vehiculo
        return vehiculo_mas_economico

    def mostrarVehiculosALaVenta(self):
        s = 'MODELO        CANTIDAD DE PUERTAS        PRECIO DE VENTA\n'
        for vehiculo in self:
            s += '%14s%27s%s\n' % (vehiculo.getModelo().ljust(14), str(vehiculo.getCantPuertas()).ljust(18), str(vehiculo.getImporteVenta()))
        print(s)

    def mostrarElementos(self):
        for i in self:
            print(i)
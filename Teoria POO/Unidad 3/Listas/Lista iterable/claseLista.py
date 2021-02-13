from claseNodo import Nodo
from claseProfesor import Profesor
class Lista:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
             self.__actual=self.__comienzo
             self.__indice=0
             raise StopIteration
        else:
             self.__indice+=1
             dato = self.__actual.getDato()
             self.__actual=self.__actual.getSiguiente()
             return dato
    def agregarProfesor(self, profesor):
        nodo = Nodo(profesor)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
    def eliminarPorDNI(self, dni):
        aux=self.__comienzo
        encontrado = False
        if aux.getDato().getDNI()==dni:
            encontrado=True
            print('Encontrado y eliminado:\n'+str(aux.getDato()))
            self.__comienzo = aux.getSiguiente()
            self.__tope-=1
            del aux
        else:
            ant = aux
            aux = aux.getSiguiente()
            while not encontrado and aux != None:
                if aux.getDato().getDNI()==dni:
                    encontrado=True
                else:
                    ant = aux
                    aux=aux.getSiguiente()
            if encontrado:
                print('Encontrado y eliminado:\n'+str(aux.getDato()))
                ant.setSiguiente(aux.getSiguiente())
                self.__tope-=1
                del aux
            else:
                print('El DNI {}, no está en la lista'.format(dni))
from claseNodo import Nodo
from interfaz import IPermisosAdmin, IPermisosUsuario
from zope.interface import implementer
from clasePersonalDeApoyo import PersonalDeApoyo
from claseDocente import Docente
from claseInvestigador import Investigador
from claseDocenteInvestigador import DocenteInvestigador
from claseObjectEncoder import objectEncoder

@implementer(IPermisosAdmin)
@implementer(IPermisosUsuario)
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

    def getCantidadElementos(self):
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
        global anterior
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
                print('Error: posición ingresada fuera de rango, la lista tiene {} componentes'.format(self.__tope))
            else:
                aux = self.__comienzo
                i = 0
                while i < posicion and aux != None:
                    aux = aux.getSiguiente()
                    i += 1
                retorno = aux.getDato()
        return retorno

    def obtenerListadoDocentesInvestigadores_xCarrera(self, carrera):
        s= 'NOMBRE         APELLIDO       CUIL        SUELDO BASICO    ANTIGUEDAD    CARRERA             CÁTEDRA             ' \
           'CARGO          AREA                TIPO                CATEGORÍA PROGRAMA    IMPORTE EXTRA\n'
        if self.__comienzo == None:
            print('La lista está vacía')
        else:
            band = False
            aux = self.__comienzo
            while aux != None:
                siguiente = aux.getSiguiente()
                agente = aux.getDato()
                if type(agente) == DocenteInvestigador:
                    if agente.getCarrera().lower() == carrera:
                        band = True
                        s += '%15s%15s%12s%17s%14s%20s%20s%15s%20s%20s%22s%s\n' % (agente.getNombre().ljust(15),
                                                                                agente.getApellido().ljust(15),
                                                                                str(agente.getCuil()).ljust(12),
                                                                                str(agente.getSueldoBasico()).ljust(17),
                                                                                str(agente.getAntiguedad()).ljust(14),
                                                                                agente.getCarrera().ljust(20),
                                                                                agente.getCatedra().ljust(20),
                                                                                agente.getCargo().ljust(15),
                                                                                agente.getArea().ljust(20),
                                                                                agente.getTipo().ljust(20),
                                                                                agente.getCategoriaPrograma().ljust(22),
                                                                                agente.getImporteExtra())
                aux = siguiente
            if band:
                print(s)
            else:
                print('No se encontraron Docentes-Investigadores que den alguna materia en la carrera: {}'.format(carrera))

    def obtenerCantidad_DocentesInvestigadores_Investigadores_xArea(self, area):
        if self.__comienzo == None:
            print('La lista está vacía')
        else:
            contI = 0
            contDI = 0
            aux = self.__comienzo
            while aux != None:
                siguiente = aux.getSiguiente()
                agente = aux.getDato()
                if type(agente) == Investigador:
                    if agente.getArea().lower() == area:
                        contI += 1
                else:
                    if type(agente) == DocenteInvestigador:
                        if agente.getArea().lower() == area:
                            contDI += 1
                aux = siguiente
            print('Cantidad de Investigadores que trabajan en el área {}: {}'.format(area, contI))
            print('Cantidad de Docentes-Investigadores que trabajan en el área {}: {}'.format(area, contDI))

    def obtenerListadoAgentes(self):
        if self.__comienzo == None:
            print('La lista está vacía')
        else:
            agentes = []
            aux = self.__comienzo
            while aux != None:
                siguiente = aux.getSiguiente()
                agente = aux.getDato()
                tipoAgente = None
                if type(agente) == PersonalDeApoyo:
                    tipoAgente = 'Personal de Apoyo'
                else:
                    if type(agente) == Docente:
                        tipoAgente = 'Docente'
                    else:
                        if type(agente) == Investigador:
                            tipoAgente = 'Investigador'
                        else:
                            if type(agente) == DocenteInvestigador:
                                tipoAgente = 'Docente-Investigador'
                agentes.append([agente.getApellido(), agente.getNombre(), tipoAgente, agente.getSueldo()])
                aux = siguiente
            agentes.sort()
            s = 'APELLIDO Y NOMBRE        TIPO DE AGENTE             SUELDO\n'
            for i in range(len(agentes)):
                nombre_apellido = agentes[i][0] + ' ' + agentes[i][1]
                s += '%25s%27s$%s\n' % (nombre_apellido.ljust(25), agentes[i][2].ljust(27), str(agentes[i][3]))
            print(s)

    def obtenerListadoDocentesInvestigadores_xCategoriaPrograma(self, categoriaPrograma):
        monto = 0
        if self.__comienzo == None:
            print('La lista esta vacía')
        else:
            s = 'APELLIDO       NOMBRE         IMPORTE EXTRA POR DOCENCIA E INVESTIGACIÓN\n'
            band = False
            aux = self.__comienzo
            while aux != None:
                siguiente = aux.getSiguiente()
                agente = aux.getDato()
                if type(agente) == DocenteInvestigador:
                    if agente.getCategoriaPrograma().lower() == categoriaPrograma:
                        band = True
                        importeExtra = agente.getImporteExtra()
                        monto += importeExtra
                        s += '%15s%15s%42s\n' % (agente.getNombre().ljust(15),
                                               agente.getApellido().ljust(15),
                                               str(importeExtra).ljust(21))
                aux = siguiente
            if band:
                print(s)
            else:
                print('No se encontraron Docentes-Investigadores de categoría {}'.format(categoriaPrograma.upper()))
        return monto

    def mostrarElementos(self):
        for i in self:
            print(i)

    def toJSON(self):
        if len(self) != 0:
            retorno = True
            lista_agentes = []
            for i in self:
                lista_agentes.append(i)
            diccionario = dict(
                __clas__=lista_agentes.__class__.__name__,
                personas=[agente.toJSON() for agente in lista_agentes]
            )
            del lista_agentes
            jsonF = objectEncoder()
            jsonF.guardarJSONArchivo(diccionario, 'personal.json')
        else:
            retorno = False
        return retorno
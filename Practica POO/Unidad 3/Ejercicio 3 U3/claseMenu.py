import datetime

from limpiarPantalla import limpiarPantalla

import csv

from claseTallerCapacitacion import tallerCapacitacion

from manejadorTalleres import manejadorTalleres

from manejadorPersonas import manejadorPersonas

from manejadorInscripciones import manejadorInscripciones

class Menu(object):
    __switcher=None
    __talleres = None
    __personas = None
    __inscripciones = None
    def __init__(self, talleres):
        self.__switcher = { 0:self.salir,
                            1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5
                         }
        self.__talleres = talleres
        self.__personas = manejadorPersonas()
        self.__inscripciones = manejadorInscripciones()
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()
    def salir(self):
        print('Chau...')

    def opcion1(self):
        if type(self.__talleres) == manejadorTalleres:
            dni = input('Ingrese el DNI de la persona: ')
            if self.__personas.buscarDNI(dni) == False:
                nom = input('Ingrese su nombre: ')
                dir = input('Ingrese su direccion: ')
                persona = self.__personas.agregarPersona(nom, dir, dni)
                limpiarPantalla()
                print(self.__talleres.getListado())
                opcion = int(input('Ingrese la opcion del taller a inscribirse: '))
                if self.__talleres.modificarCupo(opcion - 1) == True:
                    taller = self.__talleres.getTaller(opcion - 1)
                    self.__inscripciones.registrarInscripcion(persona, taller)
                    limpiarPantalla()
                    print('Incripción realizada.')
                else:
                    limpiarPantalla()
                    print('No hay cupo.')
            else:
                limpiarPantalla()
                print('La persona ya está registrada en un curso.')
        else:
            print('No hay talleres disponibles.')


    def opcion2(self):
        dni = input('Ingrese el DNI: ')
        limpiarPantalla()
        if self.__personas.buscarDNI(dni) == True:
            print(self.__inscripciones.consultarInscripcion(dni))
        else:
            print('La persona no esta inscripta a ningun taller.')

    def opcion3(self):
        idTaller = int(input('Ingrese el id del taller: '))
        limpiarPantalla()
        if self.__talleres.buscaTaller(idTaller) == True:
            print(self.__inscripciones.consultarInscripciones(idTaller))
        else:
            print('El id no corresponde a ningun taller.')

    def opcion4(self):
        dni = input('Ingrese el DNI: ')
        limpiarPantalla()
        if self.__personas.buscarDNI(dni) == True:
            self.__inscripciones.registrarPago(dni)
        else:
            print('La persona no esta inscripta a ningun taller.')

    def opcion5(self):
        self.__inscripciones.guardarInscripciones()
import csv

import numpy as np

from datetime import date

from claseInscripcion import Inscripcion

class manejadorInscripciones(object):
    __inscripciones : np.array
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self):
        self.__inscripciones = np.empty(self.__dimension, dtype=Inscripcion)

    def registrarInscripcion(self, persona, taller):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__inscripciones.resize(self.__dimension)
        self.__inscripciones[self.__cantidad] = Inscripcion(taller, persona, date.today())
        self.__cantidad += 1
        print(len(self.__inscripciones))

    def consultarInscripcion(self, dni):
        band = False
        i = 0
        while ((i < len(self.__inscripciones)) & (not band)):
            if self.__inscripciones[i].compararDni(dni) == True:
                band = True
                s = ''
                s += 'Taller: ' + self.__inscripciones[i].getNombreTaller() + '\n'
                s += 'Monto que adeuda: ' + str(self.__inscripciones[i].getMontoAdeudado())
            i += 1
        return s

    def consultarInscripciones(self, idTaller):
        band = False
        s = 'DNI             Nombre                   Direccion\n'
        for i in range(len(self.__inscripciones)):
            if type(self.__inscripciones[i]) == Inscripcion:
                if self.__inscripciones[i].compararIdTaller(idTaller) == True:
                    s += self.__inscripciones[i].getDatosPersona() + '\n'
                    band = True
        if band == False:
            s = 'No hay personas inscriptas en este taller.'
        return s

    def registrarPago(self, dni):
        band = False
        i = 0
        while ((i < len(self.__inscripciones)) & (not band)):
            if self.__inscripciones[i].compararDni(dni) == True:
                band = True
                if self.__inscripciones[i].registrarPago() == True:
                    print('Pago registrado.')
                else:
                    print('Error: la persona está al día.')
            else:
                i += 1

    def guardarInscripciones(self):
        archivo = open('inscripciones.csv', 'w', newline='')
        salida = csv.writer(archivo)
        band = False
        for i in self.__inscripciones:
            if type(i) == Inscripcion:
                salida.writerow([i.getDniPersona(), i.getIdTaller(), i.getFecha(), i.getPago()])
                band = True
        archivo.close()
        if band == True:
            print('Inscripciones guardadas.')
        else:
            print('No hay inscripciones registradas.')
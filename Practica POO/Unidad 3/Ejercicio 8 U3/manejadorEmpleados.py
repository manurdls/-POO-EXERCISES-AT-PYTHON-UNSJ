import csv
import numpy as np
from datetime import date
from datetime import datetime
from claseEmpleado import Empleado
from claseDePlanta import DePlanta
from claseContratado import Contratado
from claseExterno import Externo
from zope.interface import implementer
from interfaz import IGerente, ITesorero

@implementer(IGerente)
@implementer(ITesorero)
class manejadorEmpleados(object):
    __empleados : np.array
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension):
        self.__empleados = np.empty(dimension, dtype=Empleado)
        self.__dimension = dimension

    def cargarEmpleado(self, empleado):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__empleados.resize(self.__dimension)
        self.__empleados[self.__cantidad] = empleado
        self.__cantidad += 1

    def cargarDatos(self):
        archivo = open('planta.csv')
        reader = csv.reader(archivo, delimiter=',')
        for i in reader:
            self.cargarEmpleado(DePlanta(i[0], i[1], i[2], i[3], int(i[4]), int(i[5])))
        archivo.close()
        archivo = open('contratados.csv')
        reader = csv.reader(archivo, delimiter=',')
        for i in reader:
            if len(i) == 1:
                Contratado.modificarValorPorHora(int(i[0]))
            else:
                self.cargarEmpleado(Contratado(i[0], i[1], i[2], i[3],
                datetime.strptime(i[4], '%Y-%m-%d').date(), datetime.strptime(i[5], '%Y-%m-%d').date(), int(i[6])))
        archivo.close()
        archivo = open('externos.csv')
        reader = csv.reader(archivo, delimiter=',')
        for i in reader:
            self.cargarEmpleado(Externo(i[0], i[1], i[2], i[3],
                datetime.strptime(i[4], '%Y-%m-%d').date(), datetime.strptime(i[5], '%Y-%m-%d').date(), i[6],
                int(i[7]), int(i[8]), int(i[9])))
        archivo.close()
        del archivo

        """for i in range(self.__cantidad):
            print(self.__empleados[i])"""

    def registrarHoras(self, dni, horas):
        empleado = self.buscarEmpleadoPorDNI(dni)
        if isinstance(empleado, Empleado) == True:
            if type(empleado) == Contratado:
                empleado.sumarHoras(horas)
                print('Registro de horas realizado.')
            else:
                print('Error: el empleado no es Contratado.')
        else:
            print('Error: el DNI ingresado no corresponde a un empleado.')

    def buscarEmpleadoPorDNI(self, dni):
        band = False
        i = 0
        retorno = None
        while ((i < self.__cantidad) & (not band)):
            if self.__empleados[i].getDni() == dni:
                band = True
                retorno = self.__empleados[i]
            i += 1
        return retorno

    def totalTarea(self, tarea):
        total = 0.0
        for i in range(self.__cantidad):
            if type(self.__empleados[i]) == Externo:
                if self.__empleados[i].getTarea().lower() == tarea:
                    if self.__empleados[i].getFechaFin() >= date.today():
                        total += self.__empleados[i].sueldo()
        if total != 0:
            print('Monto a pagar: ', total)
        else:
            print('Estamos al dia.')

    def ayuda(self):
        band = False
        s = 'Nombre               Direccion                    DNI\n'
        for i in range(self.__cantidad):
            if self.__empleados[i].sueldo() < 25000.0:
                s += '%22s%29s%s\n' % (self.__empleados[i].getNombre().ljust(22),
                                     self.__empleados[i].getDireccion().ljust(29), self.__empleados[i].getDni())
                if not band:
                    band = True
        if band:
            print(s)
        else:
            print('Los empleados estan cobrando bien.')

    def sueldo(self):
        s = 'Nombre               Telefono            Sueldo\n'
        for i in range(self.__cantidad):
            s += '%22s%20s%s\n' % (self.__empleados[i].getNombre().ljust(22), self.__empleados[i].getTelefono().ljust(20),
                                   self.__empleados[i].sueldo())
        print(s)

    def gastosSueldoPorEmpleado(self, dni):
        band = False
        i = 0
        while i < self.__cantidad and not band:
            if self.__empleados[i].getDni() == dni:
                band = True
                print('Su sueldo es de: ${}'.format(self.__empleados[i].sueldo()))
            i += 1
        if not band:
            print('El número de documento no pertenece a ningún empleado')

    def modificarBasicoEPlanta(self, dni, nuevoBasico):
        empleado = self.buscarEmpleadoPorDNI(dni)
        if isinstance(empleado, Empleado):
            if type(empleado) == DePlanta:
                empleado.setSueldoBasico(nuevoBasico)
                print('La operación se realizó con éxito')
            else:
                print('Error: el DNI ingresado no corresponde a un empleado de planta')
        else:
            print('Error: el DNI ingresado no corresponde a un empleado.')

    def modificarViaticoEExterno(self, dni, nuevoViatico):
        empleado = self.buscarEmpleadoPorDNI(dni)
        if isinstance(empleado, Empleado):
            if type(empleado) == Externo:
                empleado.setMontoViatico(nuevoViatico)
                print('La operación se realizó con éxito')
            else:
                print('Error: el DNI ingresado no corresponde a un empleado externo')
        else:
            print('Error: el DNI ingresado no corresponde a un empleado.')

    def modificarValorEPorHora(self, dni, nuevoValorHora):
        empleado = self.buscarEmpleadoPorDNI(dni)
        if isinstance(empleado, Empleado):
            if type(empleado) == Contratado:
                nuevoValorHora = int(nuevoValorHora)
                empleado.modificarValorPorHora(nuevoValorHora)
                print('La operación se realizó con éxito')
            else:
                print('Error: el DNI ingresado no corresponde a un empleado contratado')
        else:
            print('Error: el DNI ingresado no corresponde a un empleado.')
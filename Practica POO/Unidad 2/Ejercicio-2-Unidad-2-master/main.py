import csv

import os

from claseViajeroFrecuente import viajeroFrecuente

from claseManejadorViajeroFrecuente import manejadorViajeroFrecuente

if __name__ == '__main__':

    listaViajeros = manejadorViajeroFrecuente()
    archivo = open('viajerosFrecuentes.csv')
    reader = csv.reader(archivo, delimiter=',')

    for fila in reader:
        viajero = viajeroFrecuente(fila[0], fila[1], fila[2], fila[3], fila[4])
        listaViajeros.agregarViajero(viajero)

    aux = None
    band = False
    num = 0
    while band is False:
        num = int(input('Ingrese  un número de viajero frecuente: '))
        aux = listaViajeros.buscarViajero(num)
        if aux is not None:
            band = True
        else:
            print('El número de viajero ingresado no pertenece a viajero alguno.')

    salir = False
    opcion = 0

    while not salir:
        os.system("cls")
        print('Numero de viajero ingresado: ', num)
        print('--------------MENU---------------')
        print("a. Mostrar cantidad de millas acumuladas")
        print("b. Acumular millas")
        print("c. Canjear millas")
        print("d. Salir\n")

        opcion = input('Ingrese una opción: ')

        if opcion == 'a':
            print('Millas acumuladas: ', aux.cantidadTotaldeMillas())

        elif opcion == 'b':
            millasRecorridas = int(input('Ingrese las millas recorridas: '))
            aux.acumularMillas(millasRecorridas)
            print('Nueva cantidad de millas: ', aux.cantidadTotaldeMillas())

        elif opcion == 'c':
            millasAcanjear = int(input('Ingrese las millas a canjear: '))
            aux.canjearMillas(millasAcanjear)
            print('Nueva cantidad de millas: ', aux.cantidadTotaldeMillas())

        elif opcion == 'd':
            salir = True
        else:
            print("Opción incorrecta.")

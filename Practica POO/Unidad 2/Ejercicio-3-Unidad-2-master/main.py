import csv

import os

from claseManejadorCamion import manejadorCamion

from claseCosecha import Cosecha

if __name__ == '__main__':



    archivo = open('camiones.csv')
    reader = csv.reader(archivo, delimiter=',')
    for fila in reader:
        mCamion = manejadorCamion(fila[0], fila[1], fila[2], fila[3], int(fila[4]))
    archivo.close()
    #print(mCamion)

    archivo = open('cosecha.csv')
    reader = csv.reader(archivo, delimiter=',')
    unaCosecha = Cosecha(reader)
    archivo.close()


    salir = False
    while not salir:
        print('---------MENU----------')
        print('1.Ingresar descarga')
        print('2.Dado Id de un camión, mostrar la cantidad total de kilos descargados')
        print('3.Dado un Día, mostrar patente, conductor, y cantidad de kilos descargados')
        print('4.Salir')

        aux = int(input('Ingrese una opción: '))
        os.system('cls')

        if aux == 1:
            #print('Opc1')
            id = int(input('Ingrese el id del camión: '))
            if (id >= 1) & (id <= 20):
                dia = int(input('Ingrese el número del día: '))
                if (dia >= 1) & (dia <= 45):
                    peso = int(input('Ingrese el peso del camión cargado, en miles de kg: '))
                    if (peso > mCamion.getCamion(id).getTara()):
                        unaCosecha.sumarDescarga(id, dia, peso, mCamion.getCamion(id).getTara())
                        print('La descarga fue registrada con éxito.')
                    else:
                        print('peso incorrecto')
                else:
                    print('dia inválido')
            else:
                print('id inválido')

        elif aux == 2:
            id = int(input('Ingrese el id del camión: '))
            if (id >= 1) & (id <=20):
                print('El camión cuyo id es: {}, descargó un total de {} kg.'.format(id, unaCosecha.getCosechaXCamion(id)))
            else:
                print('id inválido')

        elif aux == 3:
            dia = (int(input('Ingrese número de día: ')))
            print('PATENTE          CONDUCTOR           CANTIDAD DE KILOS')
            if (dia >= 1) & (dia <= 45):
                n = mCamion.getCantCamiones()
                j =1
                for i in range(n):
                    print('%16s %20s %17s' % (mCamion.getCamion(i+1).getPatente().ljust(16," "), mCamion.getCamion(i+1).getConductor().ljust(20," "),str(unaCosecha.getCosechaXDia(i+1,dia)).center(17," ")))
            else:
                print('Número de día incorrecto')

        elif aux == 4:

            archivo = open('cosecha.csv','w',newline = '')
            salida = csv.writer(archivo)
            unaCosecha.generaArchivo(salida)
            archivo.close()
            salir = True
            print('\nFIN DEL PROGRAMA')

        else:
            print('Opción Incorrecta')



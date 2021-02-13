import os
from claseFechaHora import FechaHora
from claseHora import Hora

def ingresarDatos(flag = False):

    if flag == True:
        meses = [['Enero', 31], ['Febrero', 28], ['Marzo', 31], ['Abril', 30], ['Mayo', 31], ['Junio', 30], ['Julio', 31], ['Agosto', 31], ['Septiembre', 30], ['Octubre', 31], ['Noviembre', 30], ['Diciembre', 31]]
        a = int(input('Ingrese año: '))
        if a % 4 == 0:
            if a % 100 == 0:
                if a % 400 == 0:
                    meses[1][1] = 29
            else:
                meses[1][1] = 29
        mes = int(input('Ingrese mes: '))
        while ((mes < 1) or (mes >12)):
            print('ERROR: los meses van del 1 al 12.')
            mes = int(input('Ingrese mes: '))
        d = int(input('Ingrese dia: '))
        while ((d < 1) or (d > meses[mes - 1][1])):
            if d> meses[mes - 1][1]:
                if ((mes == 2) & (meses[mes - 1][1] == 29)):
                    print('ERROR: el mes de {} tiene {} dias por ser anio bisiesto.'.format(meses[mes - 1][0], meses[mes - 1][1]))
                else:
                    print('ERROR: el mes de {} tiene {} dias.'.format(meses[mes - 1][0], meses[mes - 1][1]))
            else:
                print('ERROR: usted ingreso 0 o un numero negativo.')
            d = int(input('Ingrese dia: '))

    h = int(input('Ingrese hora: '))
    while ((h < 0) or (h>23)):
        print('ERROR: las horas van de 0 a 23')
        h = int(input('Ingrese hora: '))
    m = int(input('Ingrese minuto:'))
    while ((m < 0) or (m > 59)):
        print('ERROR: los minutos van de 0 a 59')
        m = int(input('Ingrese minuto:'))
    s = int(input('Ingrese segundos: '))
    while ((s < 0) or (s > 59)):
        print('ERROR: los segundos van de 0 a 59')
        s = int(input('Ingrese segundos: '))

    if flag == True:
        return FechaHora(d, mes, a, h, m, s)
    else:
        return [h, m, s]


if __name__ == '__main__':

    f = ingresarDatos(True)
    print(f)

    input()

    ingresarDatos()  #como estos datos no los uso no le asigno una variable
    r = Hora(f.getHora(), f.getMinutos(), f.getSegundos())
    print(r)

    input()

    f2 = f + r
    print(f2)

    input()

    f3 = r + f
    print(f3)

    input()

    f4 = f3 - 1
    print(f4)

    input()

    f4 = 1 + f2
    print(f4)

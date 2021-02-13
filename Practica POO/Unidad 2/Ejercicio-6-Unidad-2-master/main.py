import os

from claseFechaHora import FechaHora

def ingresarDatosFechaHora():

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

    return FechaHora(d, mes, a, h, m, s)

def ingresarDatosHora():
    cadena = 'ERROR: el valor debe pertenecer a N U {0}'
    h = int(input('Ingrese horas: '))
    while h < 0:
        print(cadena)
        h = int(input('Ingrese horas: '))
    m = int(input('Ingrese minutos: '))
    while m < 0:
        print(cadena)
        m = int(input('Ingrese minutos: '))
    s = int(input('Ingrese segundos: '))
    while s < 0:
        print(cadena)
        s = int(input('Ingrese segundos: '))
    return [h, m, s]

def opcion1():
    print('Ingrese los datos de la fecha y su correspondiente hora, a la que desea sumar horas minutos y segundos: ')
    objetoFechaHora = ingresarDatosFechaHora()

    print('\nIngrese el tiempo (horas, minutos, segundos) que desa sumar: ')
    hora = ingresarDatosHora()

    print('\nA la {}, se le sumara: {}h {}m {}s\n'.format(objetoFechaHora, hora[0], hora[1], hora[2]))
    objetoFechaHora + hora
    print('Resultado: ', objetoFechaHora)

def opcion2():
    print('Ingrese los datos de la fecha y su correspondiente hora, a la que desea restar horas minutos y segundos: ')
    objetoFechaHora = ingresarDatosFechaHora()

    print('\nIngrese el tiempo (horas, minutos, segundos) que desa restar: ')
    hora = ingresarDatosHora()

    print('\nA la {}, se le restara: {}h {}m {}s\n'.format(objetoFechaHora, hora[0], hora[1], hora[2]))
    objetoFechaHora - hora
    print('Resultado: ', objetoFechaHora)

def opcion3():
    print('Ingrese datos de Hora1: ')
    hora1 = ingresarDatosFechaHora()
    print('Ingrese datos de Hora2: ')
    hora2 = ingresarDatosFechaHora()
    if hora1 > hora2:
        print('Hora1 es mayor a Hora2')
    else:
        if hora2 > hora1:
            print('Hora2 es mayor a Hora1')
        else:
            print('Las horas ingresadas son iguales')

def opcion4():
    print("Chau...")


switcher = {
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':



    bandera = False
    while not bandera:
        print("\n-----------------MENU-----------------\n")
        print("1. Sumar horas")
        print("2. Restar horas")
        print("3. Dadas dos horas indicar cual es mayor")
        print("4 Salir")
        opcion= int(input("Ingrese una opción: "))
        os.system('cls')
        switch(opcion)
        bandera = int(opcion)==4

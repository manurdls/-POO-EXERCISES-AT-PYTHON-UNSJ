from claseFechaHora import FechaHora

if __name__ == '__main__':
    meses = [['Enero', 31], ['Febrero', 28], ['Marzo', 31], ['Abril', 30], ['Mayo', 31], ['Junio', 30], ['Julio', 31], ['Agosto', 31], ['Septiembre', 30], ['Octubre', 31], ['Noviembre', 30], ['Diciembre', 31]]
    a = int(input('Ingrese año: '))
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                meses[1][1] = 29
        else:
            meses[1][1] = 29
    print(meses[1][1])
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
    r = FechaHora()    # inicilizar día, mes, año con 1/1/2020, y hora, minutos y
                        # segundos con 0h, 0m, 0s.

    r1 = FechaHora(d,mes,a)    # inicializar con 0h 0m 0s
    r2= FechaHora(d,mes,a,h, m, s)
    r.Mostrar()
    r1.Mostrar()
    r2.Mostrar()

    input()

    r.PonerEnHora(5) # solamente la hora
    r.Mostrar()
    input()
    r2.PonerEnHora(13,30) #hora y minutos
    r2.Mostrar()
    input()
    r.PonerEnHora(14, 30, 25) #hora, minutos y segundos
    r.Mostrar()

    input()
    r.AdelantarHora(3) #sumar 3 horas a la hora actual
    r.Mostrar()
    input()
    r1.AdelantarHora(1,15) #sumar 1 hora y 15 minutos a la hora actual
    r1.Mostrar()
    input()

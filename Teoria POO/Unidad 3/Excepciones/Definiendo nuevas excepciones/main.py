from claseAuto import Auto
from claseErrorAuto import ErrorAuto
from claseChoqueAuto import ChoqueAuto
from claseColorNoValido import ColorNoValido

def manejarAuto(auto):
    auto.arrancar()      #arranca auto
    #auto.arrancar()        #intenta arrancar auto

    for i in range(6):
        auto.acelerar()
    choque = True       ##### cambiar
    if choque:
        velocidad = auto.getVelocidad()
        otroAuto = Auto('Toyota', 'Corolla', 2.0, 2009, 'HXT 200')
        raise ChoqueAuto(auto, otroAuto, velocidad)   ###########################

def llamarAl911():
    print('LLamar al 911')

def verColorAuto(auto):
    color = auto.getColor()
    if color == None or color == '':
        raise ColorNoValido(auto, 'El auto debe tener un color')    ##############################

def testExcepciones():
    unAuto = Auto('Renault', 'Kwid', 1.0, 2019, 'AC 123 FG')
    try:
        verColorAuto(unAuto)
    except ColorNoValido as e:
        print('ERROR')
        print('-----')
        print(e.getAuto())
        print('--------')
        print(e.getMensaje())


    try:
        manejarAuto(unAuto)
    except ChoqueAuto as e:
        if e.getVelocidad() >= 30:
            print('Accidente')
            print('---------')
            llamarAl911()
            print(e.getAuto())
            print(e.getMensaje())
    except ErrorAuto as e:
        print('ERROR')
        print('--------')
        print(e.getAuto())
        print('----------')
        print(e.getMensaje())

if __name__ == '__main__':
    testExcepciones()
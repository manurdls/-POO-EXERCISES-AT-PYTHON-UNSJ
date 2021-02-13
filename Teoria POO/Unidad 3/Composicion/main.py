from claseProfesor import Profesor

def testComposicion():
    profesor = Profesor(11334441, 'Rodríguez', 'Myriam')
    print(profesor)
    del profesor


if __name__ == '__main__':
    testComposicion()
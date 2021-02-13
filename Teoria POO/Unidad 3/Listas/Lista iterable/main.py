from claseLista import Lista
from claseProfesor import Profesor

def testLista():
    lista = Lista()
    profesor = Profesor(20201234, 'Moreno', 'Karina')
    lista.agregarProfesor(profesor)
    profesor = Profesor(11234432, 'Díaz', 'Mónica')
    lista.agregarProfesor(profesor)
    profesor = Profesor(31002008, 'Pusineri', 'Lucas')
    lista.agregarProfesor(profesor)
    for dato in lista:
        print('Datos del',dato)
    lista.eliminarPorDNI(11234432)
    print('Luego de Borrar')
    for dato in lista:
        print('Datos del',dato)
if __name__=='__main__':
    testLista()
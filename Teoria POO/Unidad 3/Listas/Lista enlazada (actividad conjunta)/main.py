from claseProfesor import Profesor
from claseLista import Lista
from claseNodo import Nodo

def testLista():
    lista = Lista()
    profesor = Profesor(20201234, 'Moreno', 'Karina',)
    lista.agregarProfesor(Profesor)
    profesor = Profesor(11234432, 'Diaz', 'Mónica')
    lista.agregarProfesor(Profesor)
    profesor = Profesor(31002008, 'Pusineri', 'Lucas')
    lista.agregarProfesor(profesor)

    lista.listarDatosProfesores()

    lista.eliminarPorDNI(11234432)
    print('Luego de borrar')

    lista.listarDatosProfesores()

if __name__ == '__main__':
    testLista()
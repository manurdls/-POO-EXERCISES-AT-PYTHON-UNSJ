from clasePunto import Punto
from claseArreglo import arregloNumPy

if __name__ == '__main__':
    arregloPuntos = arregloNumPy(3,10)
    arregloPuntos.testArregloPuntos()
    punto0 = arregloPuntos.getUnPunto(0)
    arregloPuntos.calcularDistanciasP0(punto0)
    arregloPuntos.mostrarPuntos()
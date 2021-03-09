from clasePunto import Punto
from claseLista import Lista

if __name__ == '__main__':
    listaPuntos = Lista()
    listaPuntos.testListaPuntos()
    punto0 = listaPuntos.getUnPunto(1)
    listaPuntos.calcularDistanciasP0(punto0)
    listaPuntos.mostrarPuntos()
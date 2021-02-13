from claseArreglo import Arreglo
from claseCilindro import Cilindro
from claseParalelepipedoRectangulo import ParalelepipedoRectangulo

def testPolimorfismo():
    arreglo = Arreglo()
    p = ParalelepipedoRectangulo(3,5,4)
    arreglo.agregarCuerpo(p)
    c = Cilindro(5,6)
    arreglo.agregarCuerpo(c)
    p = ParalelepipedoRectangulo(11,6,4)
    arreglo.agregarCuerpo(p)
    c = Cilindro(8,7)
    arreglo.agregarCuerpo(c)

    arreglo.calcularVolumenCuerpos()

if __name__ == '__main__':
    testPolimorfismo()
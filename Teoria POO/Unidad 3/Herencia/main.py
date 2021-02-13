from claseCirculo import Circulo
from claseCilindro import Cilindro

def testCirculoCilindro():
    circulo = Circulo(3)
    cilindro = Cilindro(5,7)
    circulo.listar()
    cilindro.listar()
    print(dir(circulo))
    print(dir(cilindro))

if __name__ == '__main__':
    testCirculoCilindro()
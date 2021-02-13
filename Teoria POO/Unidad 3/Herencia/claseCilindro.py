import math

from claseCirculo import Circulo

class Cilindro(Circulo):
    __altura = 0.0

    def __init__(self, radio, altura):
        super().__init__(radio)
        self.__altura = altura

    def superficie(self):
        superficieLateral = math.pi*2*self.getRadio()    # se puede cambiar self por super()
        superficieCirculo = super().superficie()        # no se puede cambiar super() por self xq va a intentar llamar
                                                        # al metodo superficie de Cilindro.
        return superficieLateral + 2*superficieCirculo

    def listar(self):
        print('Cilindro')
        print('Radio: {0:3.2f}, Altura: {1:3.2f}, Superficie: {2:7.5f}'.format(self.getRadio(), self.__altura, self.superficie()))
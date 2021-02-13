from limpiarPantalla import limpiarPantalla
from interfaz import IGerente

class MenuGerente(object):
    __switcher = None

    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3
                            }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, empleados):
        func = self.__switcher.get(op, lambda : print('Opcion no valida'))
        if ((op >= 1) & (op <= 3)):
            func(empleados)
        else:
            func()
    def salir(self):
        pass

    def opcion1(self, empleados):
        dni = input('Ingrese el dni: ')
        nuevoBasico = self.__ingresarMonto()
        IGerente(empleados).modificarBasicoEPlanta(dni, nuevoBasico)
    def opcion2(self, empleados):
        dni = input('Ingrese el dni: ')
        nuevoViatico = self.__ingresarMonto()
        IGerente(empleados).modificarViaticoEExterno(dni, nuevoViatico)
    def opcion3(self, empleados):
        dni = input('Ingrese el dni: ')
        nuevoValorHora = self.__ingresarMonto()
        IGerente(empleados).modificarValorEPorHora(dni, nuevoValorHora)
    def __ingresarMonto(self):
        nuevoBasico = None
        band = False
        while not band:
            try:
                nuevoBasico = float(input('Ingrese el nuevo monto: '))
                assert nuevoBasico > 0, ''
            except:
                limpiarPantalla()
                print('Error: entrada errónea')
            else:
                band = True
        return nuevoBasico
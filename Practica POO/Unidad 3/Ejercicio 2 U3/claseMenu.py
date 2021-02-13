from limpiarPantalla import limpiarPantalla

from manejadorSabores import manejadorSabores

from claseSabor import Sabor

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.salir
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op, sabores, helados):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(sabores, helados)
    def salir(self, sabores, helados):
        print('Chau...')
    def opcion1(self, sabores, helados):
        gramosPermitidos = [100, 150, 250, 500, 1000]
        sab = []

        band = False
        while not band:
            g = int(input('Ingrese los gramos: '))
            limpiarPantalla()
            aux = 0
            while ((aux < len(gramosPermitidos)) & (band == False)):
                if g == gramosPermitidos[aux]:
                    band = True
                aux += 1
            if not band:
                print('Error: gramos incorrectos')

        band = False
        aux = 0
        s = 'Error: opcion incorrecta.'
        while ((aux < 4) & (band == False)):
            band2 = False
            while not band2:
                print('Ingrese el codigo del sabor {} de 4:'.format(aux+1))
                if aux != 0:
                    print('0. Listo')
                print(sabores.getListado())
                op = int(input('Codigo: '))
                limpiarPantalla()
                if aux == 0:
                    if ((op >= 1) & (op <= sabores.getCantSabores())):
                        band2 = True
                        sab.append(sabores.getSabor(op))
                    else:
                        print(s)
                else:
                    if ((op >= 0) & (op <= sabores.getCantSabores())):
                        band2 = True
                        if op == 0:
                            aux = 4
                        else:
                            sab.append(sabores.getSabor(op))

                    else:
                        print(s)
            aux += 1
        helados.agregarHelado(g, sab)
        #helados.mostrarVendidos()





    def opcion2(self, sabores, helados):
        helados.mostrarMasPedidos(sabores)

    def opcion3(self, sabores, helados):
        band = False
        while not band:
            num = int(input('Ingrese numero de sabor: '))
            cantSabores = sabores.getCantSabores()
            if ((num >= 1) & (num <= cantSabores)):
                band = True
            else:
                print('Error: numero de sabor incorrecto.')
        limpiarPantalla()

        print('Gramos vendidos de {}: {}'.format(sabores.getNombre(num), helados.estimarGramosVendidos(num)))

    def opcion4(self, sabores, helados):
        gramosPermitidos = [100, 150, 250, 500, 1000]

        band = False
        while not band:
            g = int(input('Ingrese los gramos: '))
            limpiarPantalla()
            aux = 0
            while ((aux < len(gramosPermitidos)) & (band == False)):
                if g == gramosPermitidos[aux]:
                    band = True
                aux += 1
            if not band:
                print('Error: gramos incorrectos')
        limpiarPantalla()
        lista = helados.getNumSaboresPorTipo(g)
        if len(lista) == 0:
            print('No se vendieron sabores en ese tipo de helado.')
        else:
            s = 'Sabores vendidos en helados de ' + str(g) + 'g:'
            for i in lista:
                s += '\n' + '- ' + sabores.getNombre(i)
            print(s)
from random import randint
from limpiarPantalla import limpiarPantalla
from claseMenu import Menu
from claseLista import Lista
from interface import IInterface

if __name__ == '__main__':
    limpiarPantalla()
    lista = Lista()
    rango = randint(0, 50)
    #lista = [ randint(-1000, 1000) for i in range(0, rango)]
    for i in range(rango):
        IInterface(lista).agregarElementoFin(randint(-1000, 1000))

    print('Se ha generado una lista de {} componentes enteras'.format(rango))

    menu = Menu()
    salir = False
    while not salir:
        print('-----------------------MENU-----------------------\n'
            '0. Salir\n1. Insertar elemento\n2. Agregar elemento\n3. Mostrar elemento\n4. Mostrar lista')
        op = int(input('Ingrese una opcion: '))
        limpiarPantalla()
        menu.opcion(op, lista)
        salir = op == 0
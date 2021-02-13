from limpiarPantalla import limpiarPantalla

from manejadorHelados import manejadorHelados

from manejadorSabores import manejadorSabores

from claseMenu import Menu

if __name__ == '__main__':
    sabores = manejadorSabores()
    sabores.cargarDatos()
    #sabores.mostrarDatos()
    helados = manejadorHelados()

    menu = Menu()
    salir = False
    while not salir:
        print("\n------------Menu------------\n1. Inciso 1\n2. Inciso 2\n3. Inciso 3\n4. Inciso 4\n5. Salir")
        op = int(input('Ingrese una opcion: '))
        limpiarPantalla()
        menu.opcion(op, sabores, helados)
        salir = op == 5
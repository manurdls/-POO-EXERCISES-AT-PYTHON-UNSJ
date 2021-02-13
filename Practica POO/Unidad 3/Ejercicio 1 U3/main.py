from limpiarPantalla import limpiarPantalla

from manejadorLibros import manejadorLibros

from claseMenu import Menu

if __name__ == '__main__':
    libros = manejadorLibros()

    libros.cargarDatos()

    menu = Menu()
    salir = False
    while not salir:
        print("\n------------Menu------------\n1. Inciso 1\n2. Inciso 2\n3. Salir")
        op = int(input('Ingrese una opcion: '))
        limpiarPantalla()
        menu.opcion(op, libros)
        salir = op == 3
    print(salir)
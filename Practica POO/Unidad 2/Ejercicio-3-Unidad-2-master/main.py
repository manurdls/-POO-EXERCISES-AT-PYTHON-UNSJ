from claseManejadorCamiones import ManejadorCamiones
from claseCosecha import Cosecha
from claseMenu import Menu
from moduloLimpiarPantalla import limpiarPantalla

if __name__ == '__main__':
    cosecha = Cosecha()
    cosecha.cargarCosechaDesdeCSV('cosecha.csv')
    camiones = ManejadorCamiones()
    camiones.cargarListaDesdeCSV('camiones.csv')

    menu = Menu()
    exit = False
    while not exit:
        print("---------------MENU---------------\n"
              "1.Opción 1\n"
              "2.Opción 2\n"
              "0.Salir")
        opt = int(input('Ingrese una opción: '))
        limpiarPantalla()
        menu.opcion(opt, cosecha, camiones)
        exit = opt == 0

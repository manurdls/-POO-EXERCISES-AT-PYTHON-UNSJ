import csv
from claseMenu import Menu
from limpiarPantalla import cleanScreen

if __name__ == '__main__':
    menu = Menu()
    exit = False
    while not exit:
        print("---------------MENU---------------\n"
              "1.Registrar usuario\n"
              "2.Inciso b\n"
              "3.Inciso c\n"
              "0.Salir")
        opt = int(input('Ingrese una opcion: '))
        cleanScreen()
        menu.option(opt)
        exit = opt==0
import csv
from claseManejadorViajeroFrecuente import manejadorViajeroFrecuente
from claseViajeroFrecuente import viajeroFrecuente
from claseMenu import Menu

if __name__ == '__main__':
    ## CREO UNA INSTANCIA DEL MANEJADOR DE LOS VIAJEROS FRECUENTES
    manejaVF = manejadorViajeroFrecuente()

    ## ABRO ARCHIVO QUE CONTIENE DATOS DE VIAJEROS FRECUENTES PARA CREAR INSTANCIAS Y AGREGARLOS AL MANEJADOR
    archivo = open('viajerosFrecuentes.csv')
    reader = csv.reader(archivo, delimiter=',')
    for fila in reader:
        manejaVF.addViajero(viajeroFrecuente(fila[0], fila[1], fila[2], fila[3], fila[4]))
    archivo.close()
    ## CIERRO EL ARCHIVO

    ## INICIO CODIGO MENU DE OPCIONES
    menu = Menu()
    exit = False
    while not exit:
        id = int(input("Ingrese numero de viajero frecuente (ingrese 0 para salir): "))
        print("-----------MENU------------\n"
              "1. Consultar millas\n"
              "2. Acumular millas\n"
              "3. Canjear millas\n")
        opt = int(input("Ingrese una opcion: "))
        menu.option(opt, manejaVF)
        exit = opt==0
    ## FIN CODIGO MENU DE OPCIONES



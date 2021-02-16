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
        manejaVF.addViajero(viajeroFrecuente(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4])))
    archivo.close()
    ## CIERRO EL ARCHIVO

    ## INGRESO Y VERIFICACIÓN DE ID DE VIAJERO FRECUENTE
    id = int(input("Ingrese Id de viajero frecuente: "))
    viajero = manejaVF.buscarId(id)
    if viajero:
        ## INICIO CODIGO MENU DE OPCIONES
        menu = Menu()
        exit = False
        while not exit:
            print("-----------MENU------------\n"
                  "1. Consultar millas\n"
                  "2. Acumular millas\n"
                  "3. Canjear millas\n"
                  "0. Salir\n")
            opt = int(input("Ingrese una opcion: "))
            menu.option(opt, viajero)
            exit = opt == 0
        ## FIN CODIGO MENU DE OPCIONES

        ## TEST: este test está realizado para demostrar que el objeto devuelto del metodo buscarId del manejador
        ## devuelve una referencia al objeto que está almacenado en la lista y no una copia.
        manejaVF.consultarMillas(viajero)
        ## FINTEST
    else:
        raise TypeError("El id ingresado no pertenece a ningun Viajero Frecuente registrado.")



from limpiarPantalla import limpiarPantalla
from claseMenu import Menu
from claseObjectEncoder import objectEncoder
from interface import IInterface
from claseLista import Lista
from claseUsado import Usado
from claseNuevo import Nuevo

def cargarDatosAutos():
    autos = Lista()
    jsonF = objectEncoder()
    try:
        diccionario = jsonF.leerJSONArchivo('vehiculos.json')
    except:
        print('El archivo .json no existe')
    else:
        for i in range(len(diccionario["autos"])):
            if diccionario["autos"][i]["__class__"] == 'Nuevo':
                IInterface(autos).agregarElementoFin(Nuevo(**diccionario["autos"][i]["__atributos__"]))
            else:
                if diccionario["autos"][i]["__class__"] == 'Usado':
                    IInterface(autos).agregarElementoFin(Usado(**diccionario["autos"][i]["__atributos__"]))
    return autos

def listaToJSON(lista):
    d = dict(
        __clas__=lista.__class__.__name__,
        autos=[auto.toJSON() for auto in lista]
    )
    return d

def test():
    jsonF = objectEncoder()
    lista_autos = []
    autoUsado = Usado('FORD', 'FIESTA', 5, 'negro', 300000, 'jak 123', 2008, 100000)
    autoNuevo = Nuevo('Ford', 'Focus', 5, 'Rojo', 1200000, 'base')
    #autoNuevo2 = Nuevo('Volkswagen', 'Focus', 5, 'Rojo', 1200000, 'base') # si descomenta esto y lo agrega a la lista
    lista_autos.append(autoUsado)                                           #el programa sabe que hacer
    lista_autos.append(autoNuevo)
    #lista_autos.append(autoNuevo2)
    diccionario = listaToJSON(lista_autos)
    del lista_autos
    jsonF.guardarJSONArchivo(diccionario, 'vehiculos.json')

if __name__ == '__main__':
    limpiarPantalla()
    #test()
    autos = cargarDatosAutos()
    if len(autos) == 0:     #NOTA: esto lo hace la primera vez que abre el programa
                            #si desea que el programa arranque con autos agregados previamente
                            #descomente la funcion test() donde hay dos autos agregados, uno nuevo y uno usado
        Nuevo.setMarca(input('Ingrese la marca de los autos nuevos con la que trabaja la concesionaria:'))
    menu = Menu()
    salir = False
    while not salir:
        print('-----------------MENU-----------------\n'
              '0. Salir\n'
              '1. Insertar vehiculo\n'
              '2. Agregar vehiculo\n'
              '3. Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición\n'
              '4. Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta\n'
              '5. Mostrar todos los datos, incluido el importe de venta, del vehículo más económico\n'
              '6. Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta\n'
              '7. Almacenar los objetos de la colección Lista en el archivo “vehiculos.json”')
        op = int(input('Ingrese una opcion: '))
        limpiarPantalla()
        menu.opcion(op, autos)
        salir = op == 0
from limpiarPantalla import limpiarPantalla
from claseNuevo import Nuevo
from claseUsado import Usado
from interface import IInterface
from claseObjectEncoder import objectEncoder

class Menu(object):
    __switcher = None
    def __init__(self):
        self.__switcher = {
            0:self.salir,
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.opcion4,
            5:self.opcion5,
            6:self.opcion6,
            7:self.opcion7
        }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, autos):
        func = self.__switcher.get(op, lambda: print('Opcion no valida'))
        if op >= 1 and op <= 7:
            func(autos)
        else:
            func()

    def salir(self):
        print('Chau...')

    def opcion1(self, autos):
        vehiculo = self.__ingresarVehiculo()
        if vehiculo != None:
            print('Datos del vehiculo ingresado: \n{}'.format(vehiculo))
            posicion = self.__ingresarPosicion()
            limpiarPantalla()
            if IInterface(autos).insertarElemento(posicion, vehiculo):
                print('El vehiculo se insertó con éxito')
                #for i in autos:
                 #   print(i)
            else:
                print('El vehiculo no se pudo insertar')
                del vehiculo
        else:
            print('Error al ingresar los datos del vehiculo')
        #autos.mostrarElementos()

    def opcion2(self, autos):
        vehiculo = self.__ingresarVehiculo()
        if vehiculo != None:
            if IInterface(autos).agregarElementoFin(vehiculo):
                print('El vehiculo se agregó con éxito')
            else:
                print('El vehiculo no se pudo agregar')
                del vehiculo
        else:
            print('Error al ingresar los datos del vehiculo')
        #autos.mostrarElementos()

    def opcion3(self, autos):
        posicion = self.__ingresarPosicion()
        vehiculo = IInterface(autos).obtenerElemento_xPosicion(posicion)  ##la interfaz no implementa este metodo
        if vehiculo != None:
            print('El tipo de objeto del elemento que se en cuentra en la posicion {} es: {}'.format(posicion, type(vehiculo)))
        else:
            print('Error al obtener el vehiculo')

    def opcion4(self, autos):
        patente = input('Ingrese la patente: ')
        limpiarPantalla()
        vehiculo =IInterface (autos).obtenerElemento_xPatente(patente)  ##la interfaz no implementa este metodo
        if vehiculo != None:
            print('Modifique el precio base')
            vehiculo.setPrecioBase(float(self.__ingresarPrecioBase()))
            limpiarPantalla()
            print('El nuevo precio de venta del veliculo es: ${}'.format(vehiculo.getImporteVenta()))
        else:
            print('La patente no pertenece a ningun vehiculo')

    def opcion5(self, autos):
        vehiculo = IInterface(autos).obtenerVehiculoMasEconomico()  ##la interfaz no implementa ese metodo
        print('Vehiculo más económico:')
        print(vehiculo)
        print('Precio de venta: ${}'.format(vehiculo.getImporteVenta()))

    def opcion6(self, autos):
        interface = IInterface(autos)
        interface.mostrarVehiculosALaVenta()  ##por que me muestra si ese metodo no esta declarado en la interfaz

    def opcion7(self, autos):
        if len(autos) != 0:
            lista_autos = []
            for i in autos:
                lista_autos.append(i)
            diccionario = dict(
                __clas__=lista_autos.__class__.__name__,
                autos=[auto.toJSON() for auto in lista_autos]
            )
            del lista_autos
            jsonF = objectEncoder()
            jsonF.guardarJSONArchivo(diccionario, 'vehiculos.json')
            print('Hecho')
        else:
            print('No hay autos que guardar')

    def __ingresarVehiculo(self):
        retorno_vehiculo = None
        band = False
        while not band:
            try:
                string = input('Ingrese si el vehiculo es nuevo o usado: ').lower()
                assert string == 'nuevo' or string == 'usado', ''
            except:
                limpiarPantalla()
                print('Error: entradas válidas: nuevo o usado')
            else:
                band = True
                limpiarPantalla()
                if string == 'nuevo':
                    retorno_vehiculo = self.__cargarAutoNuevo()
                else:
                    if string == 'usado':
                        retorno_vehiculo = self.__cargarAutoUsado()
        return retorno_vehiculo

    def __cargarAutoNuevo(self):
        retorno_nuevo = None
        marca = input('Ingrese la marca: ').lower()
        limpiarPantalla()
        marca_autos_nuevos = Nuevo.getMarca()
        if marca == marca_autos_nuevos.lower():
            modelo = input('Ingrese el modelo: ')
            limpiarPantalla()
            cantPuertas = self.__ingresarCantPuertas()
            color = input('Ingrese el color: ')
            limpiarPantalla()
            precioBase = self.__ingresarPrecioBase()
            version = self.__ingresarVersion()
            retorno_nuevo = Nuevo(marca, modelo, cantPuertas, color, precioBase, version)
        else:
            print('Error: recuerde que la consecionaria es de {}'.format(marca_autos_nuevos))
        return retorno_nuevo

    def __cargarAutoUsado(self):
        retorno_usado = None
        marca = input('Ingrese la marca: ')
        limpiarPantalla()
        modelo = input('Ingrese el modelo: ')
        limpiarPantalla()
        cantPuertas = self.__ingresarCantPuertas()
        color = input('Ingrese el color: ')
        limpiarPantalla()
        precioBase = self.__ingresarPrecioBase()
        patente = input('Ingresar patente: ')
        anio = self.__ingresarAnio()
        kilometraje = self.__ingresarKilometraje()
        retorno_usado = Usado(marca, modelo, cantPuertas, color, precioBase, patente, anio, kilometraje)
        return retorno_usado

    def __ingresarCantPuertas(self):
        cantPuertas = None
        band = False
        while not band:
            try:
                cantPuertas = int(input('Ingrese la cantidad de puertas: '))
                assert cantPuertas >= 2 and cantPuertas <= 7, ''
            except ValueError:
                limpiarPantalla()
                print('Error: había que ingresar un entero')
            except:
                limpiarPantalla()
                print('Error: el auto no puede tener menos de dos puertas ni mas de siete')
            else:
                band = True
                limpiarPantalla()
        return cantPuertas

    def __ingresarPrecioBase(self):
        band = False
        while not band:
            try:
                precioBase = float(input('Ingrese el precio base: '))
                assert precioBase > 0, ''
            except ValueError:
                limpiarPantalla()
                print('Error: había que ingresar un real')
            except:
                limpiarPantalla()
                print('Error: el precio de un auto no puede ser negativo')
            else:
                band = True
                limpiarPantalla()
        return precioBase

    def __ingresarVersion(self):
        band = False
        while not band:
            try:
                version = input('Ingrese la version: ')
                assert version.lower() == 'base' or version.lower() == 'full', ''
            except ValueError:
                limpiarPantalla()
                print('Error: entrada errónea')
            except:
                limpiarPantalla()
                print('Error: las entradas admitidas son: base o full')
            else:
                band = True
                limpiarPantalla()
        return version

    def __ingresarAnio(self):
        band = False
        while not band:
            try:
                anio = int(input('Ingrese el anio del auto: '))
                assert anio >= 1980 and anio <= 2020, ''
            except ValueError:
                limpiarPantalla()
                print('Error: había que ingresar un entero')
            except:
                limpiarPantalla()
                print('Error: el anio de fabricacion del auto debe ser entre 1980 y 2020')
            else:
                band = True
                limpiarPantalla()
        return anio

    def __ingresarKilometraje(self):
        band = False
        while not band:
            try:
                kilometraje = float(input('Ingrese el kilometraje: '))
                assert kilometraje > 0, ''
            except ValueError:
                limpiarPantalla()
                print('Error: había que ingresar un real')
            except:
                limpiarPantalla()
                print('Error: el dato tiene que ser mayor a cero')
            else:
                band = True
                limpiarPantalla()
        return kilometraje

    def __ingresarPosicion(self):
        band = False
        while not band:
            try:
                posicion = int(input('Ingrese la posicion de la lista: '))
                assert posicion >= 0, ''
            except ValueError:
                limpiarPantalla()
                print('Error: habia que ingresar un entero')
            except:
                limpiarPantalla()
                print('Error: la posicion de una lista no puede ser negativa')
            else:
                band = True
                limpiarPantalla()
        return posicion
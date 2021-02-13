from limpiarPantalla import limpiarPantalla
from interfaz import IPermisosUsuario, IPermisosAdmin
from clasePersonalDeApoyo import PersonalDeApoyo
from claseDocente import Docente
from claseInvestigador import Investigador
from claseDocenteInvestigador import DocenteInvestigador


class Menu(object):
    __switcher = None

    def __init__(self):
        self.__switcher = {
            0: self.salir,
            1: self.opcion1,
            2: self.opcion2,
            3: self.opcion3,
            4: self.opcion4,
            5: self.opcion5,
            6: self.opcion6,
            7: self.opcion7,
            8: self.opcion8
        }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, permisosAdmin, permisosUsuario):
        func = self.__switcher.get(op, lambda: print('Opcion no valida'))
        if op >= 1 and op <= 2:
            func(permisosAdmin)
        else:
            if op >= 3 and op <= 8:
                func(permisosUsuario)
            else:
                func()

    def salir(self):
        print('Chau...')

    def opcion1(self, permisosAdmin):
        agente = self.__ingresarAgente()
        if agente != None:
            print('Datos del agente ingresado: \n'
                  '----------------------------\n'
                  '{}'.format(agente))
            if self.__evaluarConfirmacion() == True:
                posicion = self.__ingresarPosicion()
                limpiarPantalla()
                if permisosAdmin.insertarElemento(posicion, agente):
                    print('El agente se insertó con éxito')
                    #permisosUsuario.mostrarElementos()
                else:
                    print('Error: El agente no se pudo insertar')
                    del agente
            else:
                print('Operación cancelada')
                del agente
        else:
            print('Error: Algo ocurrió en en el ingreso de datos')

    def opcion2(self, permisosAdmin):
        agente = self.__ingresarAgente()
        if agente != None:
            print('Datos del agente ingresado: \n'
                  '----------------------------\n'
                  '{}'.format(agente))
            if self.__evaluarConfirmacion() == True:
                if permisosAdmin.agregarElementoFin(agente):
                    print('El agente se agregó con éxito')
                    #permisosUsuario.mostrarElementos()
                else:
                    print('Error: El agente no se pudo agregar')
                    del agente
            else:
                print('Operación cancelada')
                del agente
        else:
            print('Error: Algo ocurrió en en el ingreso de datos')

    def opcion3(self, permisosUsuario):
        posicion = self.__ingresarPosicion()
        agente = permisosUsuario.obtenerElemento_xPosicion(posicion)
        if agente != None:
            print('El tipo de objeto del elemento que se en cuentra en la posicion {} es: {}'.format(posicion,
                                                                                                     type(agente)))
        else:
            print('Error: algo ocurrió en la búsqueda de datos')

    def opcion4(self, permisosUsuario):
        carrera = None
        band = False
        while not band:
            try:
                carrera = input('Ingrese el nombre de una carrera: ').lower()
            except:
                limpiarPantalla()
                print('Error: entrada errónea')
            else:
                limpiarPantalla()
                band = True
        permisosUsuario.obtenerListadoDocentesInvestigadores_xCarrera(carrera)

    def opcion5(self, permisosUsuario):
        area_investigacion = None
        band = False
        while not band:
            try:
                area_investigacion = input('Ingrese el área de investigación: ').lower()
            except:
                limpiarPantalla()
                print('Error: entrada errónea')
            else:
                limpiarPantalla()
                band = True
        permisosUsuario.obtenerCantidad_DocentesInvestigadores_Investigadores_xArea(area_investigacion)

    def opcion6(self, permisosUsuario):
        permisosUsuario.obtenerListadoAgentes()

    def opcion7(self, permisosUsuario):
        categoriaPrograma = self.__ingresarCategoriaPrograma()
        monto = permisosUsuario.obtenerListadoDocentesInvestigadores_xCategoriaPrograma(categoriaPrograma.lower())
        print('El monto que se deberá solicitar al Ministerio es: ${}'.format(monto))

    def opcion8(self, permisosUsuario):
        if permisosUsuario.toJSON():
            print('Carga realizada')
        else:
            print('No hay datos que guardar')

    def __evaluarConfirmacion(self):
        confirmacion = None
        band = False
        while not band:
            try:
                confirmacion = input('Desea continuar con la operación?: ').lower()
                assert confirmacion == 'si' or confirmacion == 'no', ''
            except:
                limpiarPantalla()
                print('Error: entrada errónea')
            else:
                limpiarPantalla()
                band = True
                if confirmacion == 'si':
                    confirmacion = True
                else:
                    confirmacion = False
        return confirmacion

    def __ingresarAgente(self):
        retorno_agente = None
        band = False
        while not band:
            try:
                print('Personal que trabaja en la universidad:\n'
                      '1. Personal de apoyo\n'
                      '2. Docentes\n'
                      '3. Investigadores\n'
                      '4. Docentes-investigadores')
                opc = int(input('Ingrese la opción según el área en que se desempeña el agente a agregar: '))
                assert opc >= 1 and opc <= 4, ''
            except:
                limpiarPantalla()
                print('Error: entrada errónea')
            else:
                band = True
                limpiarPantalla()
                if opc == 1:
                    retorno_agente = self.__cargarPersonalDeApoyo()
                else:
                    if opc == 2:
                        retorno_agente = self.__cargarDocente()
                    else:
                        if opc == 3:
                            retorno_agente = self.__cargarInvestigador()
                        else:
                            if opc == 4:
                                retorno_agente = self.__cargarDocenteInvestigador()
        return retorno_agente

    def __cargarDocenteInvestigador(self):
        d = self.__cargarDatosPersona()
        carrera = input('Ingrese la carrera: ')
        limpiarPantalla()
        catedra = input('Ingrese la cátedra: ')
        limpiarPantalla()
        cargo = self.__ingresarCargo()
        limpiarPantalla()
        area = input('Ingrese el área de investigación: ')
        limpiarPantalla()
        tipo = input('Ingrese el tipo de investigación: ')
        limpiarPantalla()
        categoriaPrograma = self.__ingresarCategoriaPrograma()
        limpiarPantalla()
        importeExtra = self.__ingresarImporteExtra()
        limpiarPantalla()
        d.update(dict(
            carrera=carrera,
            catedra=catedra,
            cargo=cargo,
            area=area,
            tipo=tipo,
            categoriaPrograma=categoriaPrograma,
            importeExtra=importeExtra
        ))
        return DocenteInvestigador(**d)

    def __ingresarImporteExtra(self):
        importeExtra = None
        band = False
        while not band:
            try:
                importeExtra = float(input('Ingrese el importe extra por docencia e investigación: '))
                assert importeExtra > 0, ''
            except:
                limpiarPantalla()
                print('Error: entrada errónea')
            else:
                band = True
        return importeExtra

    def __ingresarCategoriaPrograma(self):
        categoriaPrograma = None
        band = False
        while not band:
            try:
                categoriaPrograma = input('Ingrese la categoría en el programa de incentivos de investigación: ').lower()
                assert (categoriaPrograma == 'i' or categoriaPrograma == 'ii'
                or categoriaPrograma == 'iii' or categoriaPrograma == 'iv'), ''
            except ValueError:
                limpiarPantalla()
                print('Error: entrada errónea')
            except:
                limpiarPantalla()
                print('Error: la categoría de investigación puede ser de tipo I, II, III o IV')
            else:
                band = True
        return categoriaPrograma

    def __cargarInvestigador(self):
        d = self.__cargarDatosPersona()
        area = input('Ingrese el área de investigación: ')
        limpiarPantalla()
        tipo = input('Ingrese el tipo de investigación: ')
        limpiarPantalla()
        d.update(dict(
            area=area,
            tipo=tipo
        ))
        return Investigador(**d)

    def __cargarDocente(self):
        d = self.__cargarDatosPersona()
        carrera = input('Ingrese la carrera: ')
        limpiarPantalla()
        catedra = input('Ingrese la cátedra: ')
        limpiarPantalla()
        cargo = self.__ingresarCargo()
        limpiarPantalla()
        d.update(dict(
            carrera=carrera,
            catedra=catedra,
            cargo=cargo
        ))
        return Docente(**d)

    def __ingresarCargo(self):
        cargo = None
        band = False
        while not band:
            try:
                cargo = input('Ingrese el cargo: ').lower()
                assert cargo == 'simple' or cargo == 'semiexclusivo' or cargo == 'exclusivo', ''
            except ValueError:
                limpiarPantalla()
                print('Error: entrada errónea')
            except:
                limpiarPantalla()
                print('Error: el cargo puede ser simple, semiexclusivo o exclusivo')
            else:
                band = True
        return cargo

    def __cargarPersonalDeApoyo(self):
        d = self.__cargarDatosPersona()
        categoria = self.__ingresarCategoria()
        limpiarPantalla()
        d.update(dict(
            categoria=categoria
        ))
        return PersonalDeApoyo(**d)

    def __ingresarCategoria(self):
        categoria = None
        band = False
        while not band:
            try:
                categoria = int(input('Ingrese la categoría: '))
                assert categoria >= 1 and categoria <= 22, ''
            except ValueError:
                limpiarPantalla()
                print('Error: entrada errónea')
            except:
                limpiarPantalla()
                print('Error: las categorías van de la 1 a la 22')
            else:
                band = True
        return categoria

    def __cargarDatosPersona(self):
        nombre = input('Ingrese el nombre: ')
        limpiarPantalla()
        apellido = input('Ingrese el apellido: ')
        limpiarPantalla()
        cuil = self.__ingresarCuil()
        limpiarPantalla()
        sueldoBasico = self.__ingresarSueldoBasico()
        limpiarPantalla()
        antiguedad = self.__ingresarAntiguedad()
        limpiarPantalla()
        d = dict(
            nombre=nombre,
            apellido=apellido,
            cuil=cuil,
            sueldoBasico=sueldoBasico,
            antiguedad=antiguedad
        )
        return d

    def __ingresarAntiguedad(self):
        antiguedad = None
        band = False
        while not band:
            try:
                antiguedad = int(input('Ingrese la antiguedad: '))
                assert antiguedad >= 0, ''
            except:
                limpiarPantalla()
                print('Error: entrada errónea')
            else:
                band = True
        return antiguedad

    def __ingresarSueldoBasico(self):
        sueldoBasico = None
        band = False
        while not band:
            try:
                sueldoBasico = float(input('Ingrese el sueldo básico: '))
                assert sueldoBasico >= 35000, ''
            except ValueError:
                limpiarPantalla()
                print('Error: entrada errónea')
            except:
                limpiarPantalla()
                print('Error: el sueldo básico minimo no puede ser menor a los $35000')
            else:
                band = True
        return sueldoBasico

    def __ingresarCuil(self):
        cuil = None
        band = False
        while not band:
            try:
                cuil = int(input('Ingrese el cuil: '))
                assert cuil > 0, ''
            except:
                limpiarPantalla()
                print('Error: entrada errónea')
            else:
                band = True
        return cuil

    def __ingresarPosicion(self):
        band = False
        posicion = None
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

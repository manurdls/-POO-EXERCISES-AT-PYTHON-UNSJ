from limpiarPantalla import limpiarPantalla
from interfaz import ITesorero
from claseMenuGerente import MenuGerente

class Menu(object):
    __switcher = None

    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5
                            }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, empleados):
        func = self.__switcher.get(op, lambda : print('Opcion no valida'))
        if ((op >= 0) & (op <= 5)):
            func(empleados)
        else:
            func()
    def salir(self, empleados):
        print('Chau...')

    def opcion1(self, empleados):
        dni = input('Ingrese el dni: ')
        horas = -1
        while horas < 1:
            horas = int(input('Ingrese la cantidad de horas trabajadas: '))
            limpiarPantalla()
            if horas <1:
                print('Error: el dato debe ser un entero positivo.')
        empleados.registrarHoras(dni, horas)

    def opcion2(self, empleados):
        global s
        tareas = ['carpinteria', 'electricidad', 'plomeria']
        band = False
        i = 0
        while ((i < len(tareas)) & (not band)):
            if i == 0:
                s = input('Ingrese una tarea: ')
                limpiarPantalla()
            if s.lower() == tareas[i]:
                band = True
            i += 1
            if i == 3:
                print('Error: la tarea es incorrecta.')
                i = 0
        empleados.totalTarea(s)

    def opcion3(self, empleados):
        empleados.ayuda()

    def opcion4(self, empleados):
        empleados.sueldo()

    def opcion5(self, empleados):
        usuario = input('Ingrese Usuario: ')
        passw = input('Ingrese Contraseña: ')
        limpiarPantalla()
        if usuario == 'uTesorero' and passw == 'ag@74ck':
            print('Los datos son válidos')
            dni = None
            while dni != 0:
                dni = input('Ingrese el dni del empleado, o, ingrese 0 para salir: ')
                limpiarPantalla()
                if dni != '0':
                    ITesorero(empleados).gastosSueldoPorEmpleado(dni)
                dni = int(dni)
        else:
            if usuario == 'uGerente' and passw == 'ufC77#!1':
                print('Los datos son válidos')
                menuGerente = MenuGerente()
                salir = False
                while not salir:
                    print('\n---------MENU---------\n'
                          '0. Salir\n'
                          '1. Modificar el sueldo básico de un empleado de planta\n'
                          '2. Modificar monto viático de un empleado externo\n'
                          '3. Modificar el valor por hora de un empleado contratado')
                    op = int(input('Ingrese una opcion: '))
                    limpiarPantalla()
                    menuGerente.opcion(op, empleados)
                    salir = op == 0
            else:
                print('Usuario y/o contraseña inválidos')
from limpiarPantalla import limpiarPantalla

class Menu(object):
    __switcher = None

    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4
                            }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, empleados):
        func = self.__switcher.get(op, lambda : print('Opcion no valida'))
        if ((op >= 0) & (op <= 4)):
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
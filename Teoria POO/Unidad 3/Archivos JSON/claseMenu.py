class Menu(object):
    def mostrarMenu(self):
        print('Menú de opciones: ')
        print('------------------')
        print('1 - Crear Punto')
        print('2 - Guardar Puntos en Archivo')
        print('3 - Leer datos de Puntos')
        print('4 - Mostrar datos Puntos')
        opcionCorrecta = False
        while not opcionCorrecta:
            opcion = int(input('Seleccione un numero del 1 al 5: '))
            if opcion in [1, 2, 3, 4, 5]:
                opcionCorrecta = True
        return opcion
from datetime import date

from datetime import datetime

from limpiarPantalla import limpiarPantalla

import csv

from clasePersona import Persona

from claseTallerCapacitacion import tallerCapacitacion

from claseInscripcion import Inscripcion

from manejadorTalleres import manejadorTalleres

from claseMenu import Menu

def testClaseAsociacion():
    unaPersona = Persona('Manuel Rossi', 'San Juan 785 - Jachal', '38409657')
    unTaller = tallerCapacitacion(1, 'Maneja Office como un experto', 45, 7500)
    inscripcion = Inscripcion(unaPersona, unTaller, datetime.date(2020, 5, 20) , True)

    print(inscripcion)

    talleres = manejadorTalleres(5)
    #talleres.mostrarDatos()

if __name__ == '__main__':
    #testClaseAsociacion()
    #hoy = date.today()
    #print(hoy)
    #print(type(hoy))


    archivo = open('Talleres.csv')
    reader = csv.reader(archivo, delimiter=',')
    for fila in reader:
        if len(fila) == 1:
            talleres = manejadorTalleres(int(fila[0]))
        else:
            talleres.cargarTaller(fila)
    archivo.close()

    menu = Menu(talleres)
    salir = False
    while not salir:
        print("\n------------Menu------------\n0. Salir \n1. Inscribir una persona a un taller. \n2. Consultar inscripcion. \n3. Consultar inscriptos. \n4. Registrar pago. \n5. Guardar inscripciones.")
        op = int(input('Ingrese una opcion: '))
        limpiarPantalla()
        talleres = menu.opcion(op)
        salir = op == 0
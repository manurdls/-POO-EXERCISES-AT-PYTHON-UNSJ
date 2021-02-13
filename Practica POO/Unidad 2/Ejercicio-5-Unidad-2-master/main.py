import csv

from claseAlumno import Alumno

def opcion1():
    anio = int(input('Ingrese un año: '))
    div = input('Ingrese una division: ')

    print('Alumno            Porcentaje')
    for i in range(len(listaAlumnos)):
        if listaAlumnos[i].buscaAlumno(anio, div):
            if listaAlumnos[i].getPorcentajeInasistencias() > 100:
                print ("%18s%s%s" % (listaAlumnos[i].getNombre().ljust(18, " "), str(listaAlumnos[i].getPorcentajeInasistencias()), '%'))


def opcion2():
    #Alumno.cantMaxIna = int(input('Ingrese la nueva cantidad de insasistencias permitidas: '))

    #otra opción:
    #print(Alumno.cantMaxIna)
    Alumno.cambiarCantMaxIna(int(input('Ingrese la nueva cantidad de insasistencias permitidas :')))
    #print(Alumno.cantMaxIna)

def opcion3():
    print("Fin")

switcher = {
    'a': opcion1,
    'b': opcion2,
    'c': opcion3
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':
    #alumno = Alumno('Manuel Rossi', 6, 'A', 10)
    listaAlumnos = []

    archivo = (open('alumnos.csv'))
    r = csv.reader(archivo, delimiter=';')
    for fila in r:
        listaAlumnos.append(Alumno(fila[0], int(fila[1]), fila[2], int(fila[3])))

    archivo.close()

    for i in range(len(listaAlumnos)):
        print(listaAlumnos[i])

    bandera = False # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print("")
        print("------MENU-------")
        print("a. Opción 1")
        print("b. Opción 2")
        print("c. Salir")
        opcion= input("Ingrese una opción: ")
        switch(opcion)
        bandera = opcion=='c' # Si lee el 0 cambia la bandera a true y sale del menú

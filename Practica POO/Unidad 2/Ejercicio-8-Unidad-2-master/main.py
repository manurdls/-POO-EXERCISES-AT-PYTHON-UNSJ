import csv

import os

from claseConjunto import Conjunto

def opcion1():
    print('Conjunto 1:')
    conjunto1.mostrarConjunto()
    print('Conjunto 2:')
    conjunto2.mostrarConjunto()
    union = conjunto1 + conjunto2
    print('\nUnion:')
    union.mostrarConjunto()

def opcion2():
    print('Conjunto 1:')
    conjunto1.mostrarConjunto()
    print('Conjunto 2:')
    conjunto2.mostrarConjunto()
    diferencia = conjunto1 - conjunto2
    print('\nDiferencia:')
    diferencia.mostrarConjunto()

def opcion3():
    print('Conjunto1:')
    conjunto1.mostrarConjunto()
    print('Conjunto2:')
    conjunto2.mostrarConjunto()
    if conjunto1 == conjunto2:
        print('Son iguales')
    else:
        print('Son distintos')
    print('\nConjunto2:')
    conjunto2.mostrarConjunto()
    print('Conjunto3:')
    conjunto3.mostrarConjunto()
    if conjunto2 == conjunto3:
        print('Son iguales')
    else:
        print('Son distintos')
    print('\nConjunto1:')
    conjunto1.mostrarConjunto()
    print('Conjunto4:')
    conjunto4.mostrarConjunto()
    if conjunto1 == conjunto4:
        print('Son iguales')
    else:
        print('Son distintos')


def opcion4():
    print("Adiós")


switcher = {
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':
    archivo = open('conjunto1.csv')
    reader = csv.reader(archivo, delimiter=',')
    conjunto1 = Conjunto(reader)
    archivo.close()

    archivo = open('conjunto2.csv')
    reader = csv.reader(archivo, delimiter=',')
    conjunto2 = Conjunto(reader)
    archivo.close()

    archivo = open('conjunto3.csv')
    reader = csv.reader(archivo, delimiter=',')
    conjunto3 = Conjunto(reader)
    archivo.close()

    archivo = open('conjunto4.csv')
    reader = csv.reader(archivo, delimiter=',')
    conjunto4 = Conjunto(reader)
    archivo.close()

    bandera = False
    while not bandera:
        print("\n---------------MENU--------------\n")
        print("1. Union de dos conjuntos")
        print("2. Diferencia de dos conjuntos")
        print("3. Verificar igualdad")
        print("4. Salir")
        opcion= int(input("Ingrese una opción: "))
        os.system('cls')
        switch(opcion)
        bandera = int(opcion)==4

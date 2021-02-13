import csv

from claseLibro import Libro

class manejadorLibros(object):
    __libros = []

    def __init__(self):
        self.__libros = []

    def cargarDatos(self):
        archivo = open('libros.csv')
        r = csv.reader(archivo, delimiter=',')
        aux = -1
        for i in r:
            if len(i) == 6:
                self.__libros.append(Libro(int(i[0]), i[1], i[2], i[3], int(i[4]), int(i[5])))
                aux += 1
            else:
                self.__libros[aux].agregarCapitulo(i)
        archivo.close()

    def mostrarDatos(self):
        for i in self.__libros:
            print(i)

    def buscarId(self, id):
        band = False
        aux = 0
        for i in self.__libros:
            if id == i.getId():
                band = True
                s = 'Titulo: ' + i.getTitulo()
                s += '\nCapitulos: '
                s += i.getTitulosCapitulos()
                s += '\nCantidad de paginas: ' + str(i.contarPaginas())
                print(s)
        return band

    def buscaPalabra(self, s):
        band = False
        for i in self.__libros:
            if i.getTitulo().lower().find(s.lower()) != -1:
                print('Titulo: {}, Autor: {}'.format(i.getTitulo(), i.getAutor()))
                band = True
            else:
                if i.buscaPalabra(s):
                    print('Titulo: {}, Autor: {}'.format(i.getTitulo(), i.getAutor()))
                    band = True
        if not band:
            print('La palabra ingresada no fue encontrada.')
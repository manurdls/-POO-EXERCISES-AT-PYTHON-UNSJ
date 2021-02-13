from claseCapitulo import Capitulo

class Libro(object):
    __idLibro = 0
    __titulo = ''
    __autor = ''
    __editorial = ''
    __isbn = 0
    __cantidadCapitulos = 0
    __capitulos = []

    def __init__(self, id, tit, au, ed, isbn, cantCap):
        self.__idLibro = id
        self.__titulo = tit
        self.__autor = au
        self.__editorial = ed
        self.__isbn = isbn
        self.__cantidadCapitulos = cantCap

        self.__capitulos = []


    def __str__(self):
        s = 'Id: ' + str(self.__idLibro) + '\n'
        s += 'Titulo: ' + self.__titulo + '\n'
        s += 'Autor: ' + self.__autor + '\n'
        s += 'Editorial: ' + self.__editorial + '\n'
        s += 'Isbn: ' + str(self.__isbn) + '\n'
        s += 'Cantidad de Capitulos: ' + str(self.__cantidadCapitulos)
        return s

    def agregarCapitulo(self, capitulo):
        self.__capitulos.append(Capitulo(capitulo[0], int(capitulo[1])))

    def mostrarCapitulos(self):
        for i in range(self.__cantidadCapitulos):
            print(self.__capitulos[i])

    def getId(self):
        return self.__idLibro

    def getTitulo(self):
        return self.__titulo

    def getTitulosCapitulos(self):
        s = ''
        for i in range(len(self.__capitulos)):
            s += '\n' + str(i+1) + '. ' + self.__capitulos[i].getTitulo()
        return s

    def contarPaginas(self):
        paginas = 0
        for i in self.__capitulos:
            paginas += i.getCantPaginas()
        return paginas

    def getAutor(self):
        return self.__autor

    def buscaPalabra(self, s):
        band = False
        for i in self.__capitulos:
            if i.getTitulo().lower().find(s.lower()) != -1:
                band = True
        return band
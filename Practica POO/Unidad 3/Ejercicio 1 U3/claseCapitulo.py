class Capitulo(object):
    __titulo = ''
    __cantidadPaginas = 0

    def __init__(self, tit, cant):
        self.__titulo = tit
        self.__cantidadPaginas = cant

    def __str__(self):
        return ('{} {}'.format(self.__titulo, self.__cantidadPaginas))

    def getTitulo(self):
        return self.__titulo

    def getCantPaginas(self):
        return self.__cantidadPaginas
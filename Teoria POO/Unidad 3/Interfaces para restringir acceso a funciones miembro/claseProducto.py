class Producto(object):
    __codigo = 0
    __descripcion = ''
    __precio = 0.0

    def __init__(self, codigo, descripcion, precio):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__precio = precio

    def __str__(self):
        cadena = 'Codigo Descripcion  Precio\n'
        cadena += '{0:6d} {1:15s} {2:6.2f}'.format(self.__codigo, self.__descripcion, self.__precio)
        return cadena

    def getDescripcion(self):
        return self.__descripcion

    def getCodigo(self):
        return self.__codigo

    def modificarPrecio(self, precio):
        self.__precio = precio
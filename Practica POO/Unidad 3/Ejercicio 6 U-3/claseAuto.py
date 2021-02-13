class Auto(object):
    __marca = ''
    __modelo = ''
    __cantPuertas = 0
    __color = ''
    __precioBase = 0.0

    def __init__(self, marca, modelo, cantPuertas, color, precioBase):
        self.__marca = marca.title()
        self.__modelo = modelo.title()
        self.__cantPuertas = int(cantPuertas)
        self.__color = color.title()
        self.__precioBase = float(precioBase)

    def __str__(self):
        s = 'Marca: {}\nModelo: {}\nCantidad de puertas: {}\nColor: {}\nPrecio Base: ${}\n'.format(
            self.__marca, self.__modelo, self.__cantPuertas, self.__color, self.__precioBase
        )
        return s

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getCantPuertas(self):
        return self.__cantPuertas

    def getColor(self):
        return self.__color

    def getPrecioBase(self):
        return self.__precioBase

    def setPrecioBase(self, nuevoPrecio):
        self.__precioBase = nuevoPrecio

    def reglaDeNegocio(self):
        pass

    def getImporteVenta(self):
        return self.getPrecioBase() + self.reglaDeNegocio()
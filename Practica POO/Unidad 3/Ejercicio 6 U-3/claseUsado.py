import claseAuto

class Usado(claseAuto.Auto):
    __patente = ''
    __anio = 0
    __kilometraje = 0.0

    def __init__(self, marca, modelo, cantPuertas, color, precioBase, patente, anio, kilometraje):
        super().__init__(marca, modelo, cantPuertas, color, precioBase)
        self.__patente = patente.upper()
        self.__anio = int(anio)
        self.__kilometraje = float(kilometraje)

    def __str__(self):
        s = super().__str__() + 'Patente: {}\nAnio: {}\nKilometraje: {}km'.format(
            self.__patente, self.__anio, self.__kilometraje
        )
        return s

    def getPatente(self):
        return self.__patente

    def getAnio(self):
        return self.__anio

    def getKilometraje(self):
        return self.__kilometraje

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                marca = super().getMarca(),
                modelo = super().getModelo(),
                cantPuertas = super().getCantPuertas(),
                color = super().getColor(),
                precioBase = super().getPrecioBase(),
                patente = self.__patente,
                anio = self.__anio,
                kilometraje = self.__kilometraje
            )
        )
        return d

    def reglaDeNegocio(self):
        dcto_kilometraje = 0
        dcto_antiguedad = super().getPrecioBase() * float((2020 - self.getAnio()) / 100)
        if self.__kilometraje > 100000:
            dcto_kilometraje = super().getPrecioBase() * 0.02

        return -(dcto_antiguedad + dcto_kilometraje)
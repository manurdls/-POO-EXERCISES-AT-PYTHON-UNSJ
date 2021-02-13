import claseAuto

class Nuevo(claseAuto.Auto):
    marca = None
    __version = ''

    def __init__(self, marca, modelo, cantPuertas, color, precioBase, version):
        if self.getMarca() == None:
            self.setMarca(marca.title())
        if self.getMarca().lower() == marca.lower():
            super().__init__(marca, modelo, cantPuertas, color, precioBase)
            self.__version = version.title()
        else:
            raise Exception("Los autos nuevos sólo pueden ser de la marca: {}".format(self.getMarca()))

    def __str__(self):
        s = super().__str__() + 'Version: {}'.format(self.__version)
        return s

    @classmethod
    def getMarca(cls):
        return cls.marca
    @classmethod
    def setMarca(cls, marca):
        cls.marca = marca

    def getVersion(self):
        return self.__version

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                marca = super().getMarca(),
                modelo = super().getModelo(),
                cantPuertas = super().getCantPuertas(),
                color = super().getColor(),
                precioBase = super().getPrecioBase(),
                version = self.__version
            )
        )
        return d

    def reglaDeNegocio(self):
        recarga = super().getPrecioBase() * 0.1
        if self.getVersion().lower() == 'full':
            recarga += recarga * 0.02
        return recarga
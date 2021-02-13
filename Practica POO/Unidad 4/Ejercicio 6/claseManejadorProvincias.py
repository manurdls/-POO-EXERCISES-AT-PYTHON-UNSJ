from claseProvincia import Provincia

class ManejadorProvincias(object):
    indice = 0
    __provincias = None
    def __init__(self):
        self.__provincias = []

    def mostrarProvincias(self):
        for i in self.__provincias:
            print('Nombre: {}\nCapital: {}\nCantidad de habitantes: {}\n' \
               'Cantidad de departamentos/partidos: {}\nTemperatura: {}\n' \
               'Sensación térmica: {}\nHumedad: {}\n'.format(i.getNombre(),
                                                             i.getCapital(),
                                                             i.getCantHabitantes(),
                                                             i.getCantDP(),
                                                             i.getTemperatura(),
                                                             i.getSensacionTermica(),
                                                             i.getHumedad()))


    def agregarProvincia(self, provincia):
        provincia.rowid = ManejadorProvincias.indice
        self.__provincias.append(provincia)
        self.ordenarProvincias()
        ManejadorProvincias.indice += 1

    def toUpdateDatosProvincia(self, provincia):
        provincia.setWeatherData()

    def getListaProvincias(self):
        return self.__provincias

    def ordenarProvincias(self):
        self.__provincias.sort()
        ManejadorProvincias.indice = -1
        for provincia in self.__provincias:
            ManejadorProvincias.indice += 1
            provincia.rowid = ManejadorProvincias.indice
        ManejadorProvincias.indice += 1

    def obtenerIndiceProvincia(self, provincia):
        bandera = False
        i = 0
        while not bandera and i < len(self.__provincias):
            if self.__provincias[i].rowid == provincia.rowid:
                bandera = True
            else:
                i += 1
        return i

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            provincias=[provincia.toJSON() for provincia in self.__provincias]
        )
        return d
from claseManejadorProvincias import ManejadorProvincias
from claseObjectEncoder import ObjectEncoder

class RespositorioProvincias(object):
    __conn = None
    __manejador = None
    def __init__(self, conn):
        self.__conn = conn
        diccionario = self.__conn.leerJSONArchivo()
        self.__manejador = self.__conn.decodificarDiccionario(diccionario)
        self.__manejador.ordenarProvincias()

    def obtenerListaProvincias(self):
        return self.__manejador.getListaProvincias()
    def agregarProvincia(self, provincia):
        self.__manejador.agregarProvincia(provincia)
        return provincia
    def actualizarDatosProvincia(self, provincia):
        self.__manejador.toUpdateDatosProvincia(provincia)
    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())
from claseContacto import Contacto
from claseManejadorContactos import ManejadorContactos
from claseObjectEncoder import ObjectEncoder

class RespositorioContactos(object):
    __conn = None
    __manejador = None
    def __init__(self, conn):
        self.__conn = conn
        diccionario = self.__conn.leerJSONArchivo()
        self.__manejador = self.__conn.decodificarDiccionario(diccionario)

    def to_values(self, contacto):
        return contacto.getApellido(), contacto.getNombre(), contacto.getEmail(), contacto.getTelefono()
    def obtenerListaContactos(self):
        return self.__manejador.getListaContactos()
    def agregarContacto(self, contacto):
        self.__manejador.agregarContacto(contacto)
        return contacto
    def modificarContacto(self, contacto):
        self.__manejador.updateContacto(contacto)
        return contacto
    def borrarContacto(self, contacto):
        self.__manejador.deleteContacto(contacto)
    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())

### yo creo que aca es donde hay que testear toda la parte de  "El Modelo" ##
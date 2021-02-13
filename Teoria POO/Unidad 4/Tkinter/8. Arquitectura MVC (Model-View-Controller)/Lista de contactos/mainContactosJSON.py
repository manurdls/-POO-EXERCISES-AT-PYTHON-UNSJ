
from claseContacto import Contacto
from claseManejadorContactos import ManejadorContactos
from claseObjectEncoder import ObjectEncoder
def testContactos(manejadorC):
    contacto1=Contacto('Rueda', 'Melisa', 'melisarueda@gmail.com', '(264)4777222')
    contacto2=Contacto('López', 'Carlos', 'carloslopez@yahoo.com', '(261)4888111')
    contacto3=Contacto('Pérez', 'Maira', 'mariaperez@hotmail.com', '(264)5111222')
    contacto4=Contacto('Altamirano', 'Sandra', 'altamiranos@microsoft.com','(263)6478912')
    contacto5=Contacto('Artime', 'Luis','luifa@elcomercio.com', '(264)4558699')
    manejadorC.agregarContacto(contacto1)
    manejadorC.agregarContacto(contacto2)
    manejadorC.agregarContacto(contacto3)
    manejadorC.agregarContacto(contacto4)
    manejadorC.agregarContacto(contacto5)



if __name__=='__main__':
    jF = ObjectEncoder('contactos.json')
    manejador=ManejadorContactos()
    testContactos(manejador)
    diccionario=jF.leerJSONArchivo()
    manejador=jF.decodificarDiccionario(diccionario)
    #manejador.mostrarContactos()
    #diccionarioManejador=manejador.toJSON()
    #jF.guardarJSONArchivo(diccionarioManejador)
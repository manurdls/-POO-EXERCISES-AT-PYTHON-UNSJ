from claseProvincia import Provincia
from claseManejadorProvincias import ManejadorProvincias
from claseObjectEncoder import ObjectEncoder
def testProvincias(manejadorP):
    provincia1=Provincia('San Juan', 'San Juan', '738959', '19')
    provincia2=Provincia('Chubut', 'Rawson', '556319', '12')
    #provincia3=Provincia('Mendoza', 'Mendoza', '232434', '36')
    manejadorP.agregarProvincia(provincia1)
    manejadorP.agregarProvincia(provincia2)
    #manejadorP.agregarProvincia(provincia3)
    #manejadorP.mostrarProvinciasRowid()


if __name__=='__main__':
    jF = ObjectEncoder('datos.json')
    manejador = ManejadorProvincias()
    testProvincias(manejador)

    #diccionario=jF.leerJSONArchivo()
    #manejador=jF.decodificarDiccionario(diccionario)
    #manejador.mostrarProvincias()
    diccionarioManejador=manejador.toJSON()
    jF.guardarJSONArchivo(diccionarioManejador)
from claseObjectEncoder import objectEncoder
from claseManejador import Manejador
from clasePunto import Punto
from claseMenu import Menu

if __name__ == '__main__':
    jsonF = objectEncoder()
    puntos = Manejador()
    bandera = True
    while bandera:
        menu = Menu()
        opcion = menu.mostrarMenu()
        if opcion == 1:
            print('Creando un nuevo punto')
            x = int(input('Coordenada x: '))
            y = int(input('Coordenada y: '))
            punto = Punto(x, y)
            puntos.agregarPunto(punto)
        else:
            if opcion == 2:
                d = puntos.toJSON()
                jsonF.guardarJSONArchivo(d, 'datosPuntos.json')
            else:
                if opcion == 3:
                    diccionario = jsonF.leerJSONArchivo('datosPuntos.json')
                    diccionario = jsonF.decodificarDiccionario(diccionario)
                    print(diccionario)
                else:
                    if opcion == 4:
                        puntos.mostrarDatos()
                    else:
                        bandera = False
                        print('Chau...')
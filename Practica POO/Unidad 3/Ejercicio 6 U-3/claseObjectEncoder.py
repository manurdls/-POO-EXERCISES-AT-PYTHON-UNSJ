import json
from pathlib import Path

class objectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'list':
                puntos = d['puntos']
                dPunto = puntos[0]
                manejador = class_()
                for i in range(len(puntos)):
                    dPunto = puntos[i]
                    class_name = dPunto.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dPunto['__atributos__']
                    unPunto = class_(**atributos)
                    manejador.agregarPunto(unPunto)
        return manejador

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)
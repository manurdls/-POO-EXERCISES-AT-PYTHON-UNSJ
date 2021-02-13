from clasePersona import Persona

class manejadorPersonas(object):
    __personas = None

    def __init__(self):
        self.__personas = []

    def agregarPersona(self, nom, dir, dni):
        persona = Persona(nom, dir, dni)
        self.__personas.append(persona)
        return persona

    def buscarDNI(self, dni):
        band = False
        i = 0
        while ((i < len(self.__personas)) & (not band)):
            if dni == self.__personas[i].getDNI():
                band = True
            i += 1
        return band

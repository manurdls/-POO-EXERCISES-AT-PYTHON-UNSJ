import datetime

from clasePersona import Persona

from claseTallerCapacitacion import tallerCapacitacion

class Inscripcion(object):
    __fechaInscripcion : datetime.date
    __pago : bool
    __persona : Persona
    __taller : tallerCapacitacion

    def __init__(self, taller, persona, fecha, pago = False):
        self.__fechaInscripcion = fecha
        self.__pago = pago
        self.__persona = persona
        self.__taller = taller

    def __str__(self):
        s = ''
        if self.__pago == True:
            s += 'Si'
        else:
            s += 'No'
        return 'Persona: ' + self.__persona.getNombre() + '\nTaller: ' + self.__taller.getNombre() + '\nFecha de Inscripcion: ' + str(self.__fechaInscripcion) + '\nPago?: ' + s

    def getFecha(self):
        return self.__fechaInscripcion

    def getPago(self):
        return self.__pago

    def compararDni(self, dni):
        band = False
        if self.__persona.getDNI() == dni:
            band = True
        return band

    def getNombreTaller(self):
        return self.__taller.getNombre()

    def getMontoAdeudado(self):
        monto = 0
        if self.__pago == False:
            monto = self.__taller.getMontoInscripcion()
        return monto

    def compararIdTaller(self, idTaller):
        band = False
        if self.__taller.getId() == idTaller:
            band = True
        return band

    def getDatosPersona(self):
        s = '%16s%25s%s' % (self.__persona.getDNI().ljust(16), self.__persona.getNombre().ljust(25), self.__persona.getDireccion())
        return s

    def registrarPago(self):
        band = False
        if self.__pago == False:
            self.__pago = True
            band = True
        return band

    def getDniPersona(self):
        return self.__persona.getDNI()

    def getIdTaller(self):
        return self.__taller.getId()
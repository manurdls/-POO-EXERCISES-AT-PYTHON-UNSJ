from claseActaDeNacimiento import ActaNacimiento
class RegistroCivil:
        __denominacion=''
        __domicilio=''
        __actas=None
        # Variables de clase
        actaActual = 100
        libroActual = 5
        def __init__(self, denominacion, domicilio):
            self.__denominacion = denominacion
            self.__domicilio = domicilio
            self.__actas=[]
        # Métodos de clase
        @classmethod
        def getActaActual(cls):
            cls.actaActual+=1
            return cls.actaActual
        @classmethod
        def getLibroActual(cls):
            return cls.libroActual
        # Métodos de instancia
        def inscribirPersona(self, persona, fecha):
            numeroActa = self.getActaActual()
            libro = self.getLibroActual()
            acta = ActaNacimiento(numeroActa, libro, fecha, persona, self)
            self.__actas.append(acta)
        def mostrarActas(self):
            for acta in self.__actas:
                print(acta)
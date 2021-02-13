import re

class Paciente(object):
    telefonoRegex = re.compile(r"\([0-9]{3}\)[0-9]{7}")
    __apellido = None
    __nombre = None
    __telefono = None
    __altura = None
    __peso = None
    __imc = None
    __compCorporal = None
    def __init__(self, apellido, nombre, telefono, altura, peso):
        self.__apellido = self.requerido(apellido, 'Apellido es un valor requerido')
        self.__nombre = self.requerido(nombre, 'Nombre es un valor requerido')
        self.__telefono = self.formatoValido(telefono, Paciente.telefonoRegex, 'Telefono no tiene formato correcto')
        self.__altura = self.requerido(altura, 'Altura es un valor requerido')
        self.__peso = self.requerido(peso, 'Peso es un valor requerido')
        self.__imc = self.__calcularIMC(float(self.__altura), float(self.__peso))
        self.__compCorporal = self.__calcularCompCorporal(self.__imc)
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getTelefono(self):
        return self.__telefono
    def getAltura(self):
        return self.__altura
    def getPeso(self):
        return self.__peso
    def getIMC(self):
        return self.__imc
    def getCompCorporal(self):
        return self.__compCorporal
    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    def formatoValido(self, valor, regex, mensaje):
        if not valor or not regex.match(valor):
            raise ValueError(mensaje)
        return valor
    def __calcularIMC(self, altura, peso):
        altura = altura / 100
        imc = round(peso / (altura * altura), 1)
        return imc
    def __calcularCompCorporal(self, imc):
        compCorp = None
        if imc < 18.5:
            compCorp = 'Peso inferior al normal'
        else:
            if imc >= 18.5 and imc < 25.0:
                compCorp = 'Normal'
            else:
                if imc >= 25.0 and imc < 30.0:
                    compCorp = 'Peso superior al normal'
                else:
                    if imc >= 30:
                        compCorp = 'Obesidad'
        return compCorp


    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                apellido=self.__apellido,
                nombre=self.__nombre,
                telefono=self.__telefono,
                altura=self.__altura,
                peso=self.__peso
            )
        )
        return d
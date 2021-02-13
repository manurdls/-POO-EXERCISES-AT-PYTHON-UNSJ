import re

class Contacto(object):
    emailRegex = re.compile(r"[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}")
    telefonoRegex = re.compile(r"\([0-9]{3}\)[0-9]{7}")
    __apellido = None
    __nombre = None
    __email = None
    __telefono = None
    def __init__(self, apellido, nombre, email, telefono):
        print(apellido)
        self.__apellido = self.requerido(apellido, 'Apellido es un valor requerido')
        self.__nombre = self.requerido(nombre, 'Nombre es un valor requerido')
        self.__email = self.formatoValido(email, Contacto.emailRegex, 'Email no tiene formato correcto')
        self.__telefono = self.formatoValido(telefono, Contacto.telefonoRegex, 'Telefono no tiene formato correcto')
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getEmail(self):
        return self.__email
    def getTelefono(self):
        return self.__telefono

    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor
    def formatoValido(self, valor, regex, mensaje):
        if not valor or not regex.match(valor):
            raise ValueError(mensaje)
        return valor

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                apellido=self.__apellido,
                nombre=self.__nombre,
                email=self.__email,
                telefono=self.__telefono
            )
        )
        return d
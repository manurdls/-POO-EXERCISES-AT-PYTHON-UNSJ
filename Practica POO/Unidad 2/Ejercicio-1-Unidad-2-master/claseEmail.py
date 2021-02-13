import re

class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contrasema = ''

    def __init__(self, id='', dom='', tipo='', passw=''):
        self.__idCuenta = id
        self.__dominio = dom
        self.__tipoDominio = tipo
        self.__contrasena = passw

    def __str__(self):          #utilizo este método en vez de retornaEmil()
        return self.__idCuenta + '@' + self.getDominio() + '.' + self.__tipoDominio

    def getDominio(self):
        return self.__dominio

    def crearCuenta(self, email):
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',email.lower()):

            self.__idCuenta = email[:email.find("@")]
            self.__dominio = email[email.find("@") + 1:email.find(".")]
            self.__tipoDominio = email[email.find(".") + 1:]

            print('El objeto fue creado exitosamente')
        else:
            print('ERROR: el formato del mail es invalido')
            return False
        return True


    def modificarContrasena(self, passvieja):
        if passvieja == self.__contrasena:
            self.__contrasena = input('Ingrese nueva contraseña:')
            print('La contraseña se cambió correctamente')
        else:
            print('ERROR: la contraseña ingresada es incorrecta')



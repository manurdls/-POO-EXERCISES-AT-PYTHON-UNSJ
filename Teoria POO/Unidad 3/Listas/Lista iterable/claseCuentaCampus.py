class CuentaCampus:
    dominio='@unsj-cuim.edu.ar'
    idCuenta=0
    __idUsuario=0
    __nombreUsuario=''
    __clave=''
    @classmethod
    def getDominio(cls):
        return cls.dominio
    @classmethod
    def getIdCuenta(cls):
        cls.idCuenta+=1
        return cls.idCuenta
    def __init__(self, idUsuario, nombreUsuario, clave):
        self.__idUsuario=idUsuario
        self.__nombreUsuario=nombreUsuario
        self.__clave=clave
    def __str__(self):
        cadena = 'Usuario: {}\nClave {}'.format(self.__nombreUsuario, self.__clave)
        return cadena
    def cambiarClave(self, nuevaClave):
        self.__clave=nuevaClave
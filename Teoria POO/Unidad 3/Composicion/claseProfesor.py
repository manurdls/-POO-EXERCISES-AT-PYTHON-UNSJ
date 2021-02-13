from claseCuentaCampus import CuentaCampus

class Profesor:
    __dni=0
    __apellido=''
    __nombre=''
    __cuentaCampus=None
    def __init__(self, dni, apellido, nombre):
        self.__dni=dni
        self.__apellido=apellido
        self.__nombre=nombre
        idCuenta=CuentaCampus.getIdCuenta()
        dominio=CuentaCampus.getDominio()
        usuario=nombre.lower()+apellido.lower()+dominio
        self.__cuentaCampus=CuentaCampus(idCuenta,usuario,dni) #en la composició el objeto se crea dentro del objeto que lo contiene
    def __del__(self):
        print('Borrando cuenta de usuario....')
        #del self.__cuentaCampus    #al crearse el objeto de cuentaCampus dentro de este objeto (por ser composicion)
                                    #al eliminar el objeto 'todo' tambien se elimina el objeto 'parte' automaticamente
                                    #esto se puede comprobar facilmente en este metodo, tenga o no tenga el numeral
                                    #el destructor del objeto 'parte' se llama automaticamente.
    def __str__(self):
        cadena ='Profesor: \n'
        cadena += 'Apellido y nombre: {}, {}\n'.format(self.__apellido, self.__nombre)
        cadena+=str(self.__cuentaCampus)
        return cadena
    def getDNI(self):
        return self.__dni

    def getCuentaCampus(self):
        return self.__cuentaCampus
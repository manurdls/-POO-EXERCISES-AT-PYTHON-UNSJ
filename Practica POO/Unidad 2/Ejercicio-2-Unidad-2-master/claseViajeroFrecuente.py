

class viajeroFrecuente():
    __id = 0
    __name = ""
    __surname = ""
    __dni = ""

    def  __init__(self, id, nombre, apellido, dni):
        verificacionDatos = True
        if verificacionDatos:
            self.__id = id
            self.__name = nombre
            self.__surname = apellido
            self.__dni = dni
        else:
            raise TypeError "El formato de algún parametro de entrada es incorrecto"

    


class viajeroFrecuente():
    __id = 0
    __name = ""
    __surname = ""
    __dni = ""
    __miles = 0

    def  __init__(self, id, nombre, apellido, dni, miles=0):
        verificacionDatos = True
        if verificacionDatos:
            self.__id = id
            self.__name = nombre
            self.__surname = apellido
            self.__dni = dni
            self.__miles = miles
        else:
            raise TypeError("El formato de algún parametro de entrada es incorrecto")

    def getId(self):
        return self.__id

    def getMiles(self):
        return self.__miles

    def acumularMiles(self, miles):
        if isinstance(miles, int):
            if miles > 0:
                self.__miles += miles
                print("Millas acumuladas, cantidad actual de millas: {}".format(self.getMiles()))
            raise ValueError("Se esperaba un entero positivo")
        else:
            raise TypeError("Se esperaba un entero")

    def canjearMiles(self, miles):
        if isinstance(miles, int):
            if miles <= self.__miles:
                self.__miles -= miles
                print("MIllas canjeadas, cantidad actual de millas: {}".format(self.getMiles()))
            else:
                print("Error: cantidad de millas insuficientes")
        else:
            raise TypeError("Se esperaba un entero")





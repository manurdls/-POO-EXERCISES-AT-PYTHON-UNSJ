class viajeroFrecuente:
    __idViajero: 0
    __nombre: ''
    __apellido: ''
    __dni: ''
    __millasAcumuladas= 0

    def __init__(self, idV, nom, ap, dni, mill):
        self.__idViajero = int(idV)
        self.__nombre = nom
        self.__apellido = ap
        self.__dni = dni
        self.__millasAcumuladas = int(mill)

    def __str__(self):
        return '\nEstado del objeto.\nId: {}\nNombre: {}\nApellido: {}\nDNI: {}\nMillas Acumuladas: {}'.format(
            self.__idViajero, self.__nombre, self.__apellido, self.__dni, self.__millasAcumuladas)

    def cantidadTotaldeMillas(self):
        return self.__millasAcumuladas

    def acumularMillas(self, millasRecorridas):
        if type(millasRecorridas) == int:
            self.__millasAcumuladas += millasRecorridas
        else:
            print('ERROR: se esperaba un numero entero.')

    def canjearMillas(self, millasAcanjear):
        if type(millasAcanjear) == int:
            if millasAcanjear <= self.__millasAcumuladas:
                self.__millasAcumuladas -= millasAcanjear
                print('Las millas se canjearon correctamente.')
            else:
                print('No dispone de millas suficientes para efectuar el canje.')
        else:
            print('ERROR: se esperaba un numero entero.')

    def mostrarId(self):
        return self.__idViajero


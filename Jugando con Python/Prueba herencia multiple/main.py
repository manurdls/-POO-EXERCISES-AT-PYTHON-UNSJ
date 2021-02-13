class Padre(object):  # Creamos la clase Padre
    def __init__(self, ojos, cejas):  # Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas


class Madre(object):  # Creamos la clase Padre
    def __init__(self, brazos, piernas):  # Definimos los Atributos
        self.brazos = brazos
        self.piernas = piernas


class Hijo(Padre, Madre):  # Creamos clase hija que hereda de Padre y luego de Madre
    def __init__(self, ojos, cejas, cara, brazos, piernas):  # creamos el constructor de la clase especificando atributos
        super(Madre, self).__init__(self, brazos, piernas)
        super(Padre, self).__init__(self, ojos, cejas)  # Solicitamos a super llamar de la clase padre esos atributos
        self.cara = cara


Tomas = Hijo('Marrones', 'Negras', 'Larga', 2, 2)
print(Tomas.ojos, Tomas.cejas, Tomas.cara, Tomas.piernas, Tomas.brazos)
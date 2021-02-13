class Alumno:
    #atributos de clase
    cantMaxIna = 20
    cantTotClases = 200

    #atributos de instancia
    __nombre = ''
    __anio = 0
    __division = ''
    __cantIna = 0

    def __init__(self, n, a, d, c):
        self.__nombre = n
        self.__anio = a
        self.__division = d
        self.__cantIna = c
        print(type(self.__division))

    def __str__(self):
        return 'Inasistencias posibles: {}, Cantidad de clases anuales: {}, Nombre: {}, Año: {}, Division: {}, Inasistencias: {}'.format(self.cantMaxIna, self.cantTotClases, self.__nombre, self.__anio, self.__division, self.__cantIna)

    def buscaAlumno(self, anio, d):
        band = False
        if ((self.__anio == anio) & (self.__division == d)):
            band = True
        return band

    def getPorcentajeInasistencias(self):
        return ((self.__cantIna*100)/self.cantMaxIna)

    def getNombre(self):
        return self.__nombre

    @classmethod
    def cambiarCantMaxIna(cls, nuevoValor):
        cls.cantMaxIna = nuevoValor


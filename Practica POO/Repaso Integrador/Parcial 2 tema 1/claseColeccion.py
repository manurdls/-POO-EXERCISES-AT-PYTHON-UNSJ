import numpy as np
from claseEmpleado import Empleado
from claseDocente import Docente
from clasePau import Pau


class Coleccion(object):
    __empleados = None
    __cantidad = 0
    __dimension = 0
    __incremento = 5

    def __init__(self, dimension, incremento=5):
        self.__empleados = np.empty(dimension, Empleado)
        self.__dimension = dimension
        self.__incremento = incremento

    def agregarEmpleado(self, empleado):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__empleados.resize(self.__dimension)
        self.__empleados[self.__cantidad] = empleado
        self.__cantidad += 1

    def incisoDos(self):
        total = 0
        for i in range(self.__cantidad):
            if isinstance(i, Pau):
                total += Pau.monotoHorasExtra*i.getHorasExtra()

        print('El importe total que debera abonar la Universidad sera: {}$'.format(float(total)))

    def incisoTres(self, dependencia):
        contDocentes = 0
        contPau = 0
        for i in range(self.__cantidad):
            if dependencia == i.getDependencia():
                if isinstance(i, Docente):
                    contDocentes += 1
                else:
                    contPau += 1
        print('Cantidad de Docentes: {}\nCantidad de Pau: {}\n'.format(contDocentes, contPau))

    def incisoCuatro(self):
        for i in range(self.__cantidad):
            string = 'Nombre: {}\nApellido: {}\nDependencia: {}\nSalario: {}\n'.format(i.getNombre,
                                                                                       i.getApellido,
                                                                                       i.getDependencia,
                                                                                       i.getSalario)




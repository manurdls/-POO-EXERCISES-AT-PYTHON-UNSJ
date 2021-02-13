from claseNodo import Nodo
from claseEmpleado import Empleado
from claseRepositor import Repositor
from claseDependiente import Dependiente

class Coleccion(object):
    __comienzo = None

    def __init__(self):
        self.__comienzo = None

    def agregarEmpleado(self, empleado):
        nodo = Nodo(empleado)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo

    def incisoDos(self):
        aux = self.__comienzo
        total = 0
        while aux != None:
            empleado = aux.getEmpleado()
            if empleado.getTurno() == "noche":
                total += 150
                empleado = aux.getEmpleado()
            if isinstance(empleado, Repositor):
                empleado = aux.getEmpleado()
                total += empleado.reglaDeNegocio()
            aux = aux.getSiguiente()

        print("Importe extra: {}".format(total))

    def incisoTres(self):
        aux = self.__comienzo
        cant = 0
        while aux != None:
            empleado = aux.getEmpleado()
            if isinstance(empleado, Dependiente):
                if empleado.getEspecialidad() == 'caja' and empleado.getTurno() == 'noche':
                    cant += 1
            aux = aux.getSiguiente()

        print("Cantidad: {}".format(cant))

    def incisoCuatro(self):
        aux = self.__comienzo
        while aux != None:
            empleado = aux.getEmpleado()
            print('Apellido: {}\nNombre: {}\nSalario: ${}'.format(empleado.getApellido(), empleado.getNombre(), empleado.getSueldo()))
            aux = aux.getSiguiente()

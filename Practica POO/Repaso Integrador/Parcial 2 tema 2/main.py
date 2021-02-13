from claseColeccion import Coleccion
from claseDependiente import Dependiente
from claseRepositor import Repositor

def test(coleccion):
    dependiente1 = Dependiente("Rossi", "Manuel", 20000, 5, 'noche', 'caja')
    dependiente2 = Dependiente("Berreta", "Florencia", 20000, 8, 'noche', 'fiambreria')
    repositor1 = Repositor("Silvina", "de los Santos", 45000, 20, 'noche', 70, 'Escuela Normal')
    repositor2 = Repositor("Patricia", "Porto", 31000, 2, 'maniana', 31, 'Hospital Rawson')

    coleccion.agregarEmpleado(dependiente1)
    coleccion.agregarEmpleado(dependiente2)
    coleccion.agregarEmpleado(repositor1)
    coleccion.agregarEmpleado(repositor2)

    coleccion.incisoDos()
    coleccion.incisoTres()
    coleccion.incisoCuatro()


if __name__ == '__main__':
    coleccion = Coleccion()
    test(coleccion)
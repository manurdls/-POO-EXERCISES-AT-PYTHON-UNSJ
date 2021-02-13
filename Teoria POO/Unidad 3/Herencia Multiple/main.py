from clasePersona import Persona
from claseDocente import Docente
from claseAlumno import Alumno
from claseAyudante import Ayudante

def testHerenciaMultiple():
    print('MRO de la clase ayudante: ',Ayudante.mro())
    ayudante = Ayudante(38409657, 'Rossi', 'Manuel', '20/03/2019', 9, 'LCC', 3211, 90, 'POO', 2500, 'Sobresaliente', 5)
    ayudante.mostrarDatos()

if __name__ == '__main__':
    testHerenciaMultiple()
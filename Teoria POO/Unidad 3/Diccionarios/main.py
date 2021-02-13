from claseAlumno import Alumno

if __name__ == '__main__':
    diccionario = dict({'registro':12345, 'nombre':'Carla', 'apellido':'Ibaceta', 'carrera':'LCC'})
    unAlumno = Alumno(**diccionario)
    print(unAlumno)
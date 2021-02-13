from limpiarPantalla import limpiarPantalla
from claseMenu import Menu
from claseDocente import Docente
from claseInvestigador import Investigador
from clasePersonalDeApoyo import PersonalDeApoyo
from claseDocenteInvestigador import DocenteInvestigador
from claseObjectEncoder import objectEncoder
from claseLista import Lista
from interfaz import IPermisosAdmin, IPermisosUsuario

def mostrarMenu():
    print('-------------------MENU-------------------\n'
          '0. Salir\n'
          '1. Insertar agente a la colección\n'
          '2. Agregar agente a la colección\n'
          '3. Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición\n'
          '4. Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos'
          ' de los agentes que se desempeñan como docentes investigadores\n'
          '5. Dada un área de investigación, contar la cantidad de agentes que son docente-investigador,'
          ' y la cantidad de investigadores que trabajen en ese área.\n'
          '6. Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente'
          ' y sueldo de todos los agentes, ordenado por apellido\n'
          '7. Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado,'
          ' listar apellido, nombre e importe extra por docencia e investigación,'
          ' de todos los docentes investigadores que poseen esa categoría,'
          ' al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación'
          ' debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores'
          ' de la categoría solicitada\n'
          '8. Almacenar los datos de todos los agentes en el archivo “personal.json”')

def cargarDatosPersonal(interfaz):
    jsonF = objectEncoder()
    try:
        diccionario = jsonF.leerJSONArchivo('personal.json')
    except:
        print('El archivo .json no existe')
    else:
        for i in range(len(diccionario["personas"])):
            if diccionario["personas"][i]["__class__"] == 'PersonalDeApoyo':
                interfaz.agregarElementoFin(PersonalDeApoyo(**diccionario["personas"][i]["__atributos__"]))
            else:
                if diccionario["personas"][i]["__class__"] == 'Docente':
                    interfaz.agregarElementoFin(Docente(**diccionario["personas"][i]["__atributos__"]))
                else:
                    if diccionario["personas"][i]["__class__"] == 'Investigador':
                        interfaz.agregarElementoFin(Investigador(**diccionario["personas"][i]["__atributos__"]))
                    else:
                        if diccionario["personas"][i]["__class__"] == 'DocenteInvestigador':
                            interfaz.agregarElementoFin(DocenteInvestigador(**diccionario["personas"][i]["__atributos__"]))

def listaToJSON(lista):
    d = dict(
        __clas__=lista.__class__.__name__,
        personas=[persona.toJSON() for persona in lista]
    )
    return d

def test():
    personalDeApoyo = PersonalDeApoyo('Eduardo', 'Riveros', 1, 45000, 7, 22)
    docente = Docente('Jorge','Fernandez',2,60000,10,'Geofisica','Geofisica de pozo','exclusivo')
    investigador = Investigador('Luciana','Rodriguez',3,60000,3,'Informatica','Algoritmia')
    docenteInvestigador = DocenteInvestigador('Mariana','Estrada',4,65000,15,'Licenciatura en ciencias de la computacion',
                                              'Programacion procedural','exclusivo','Informatica','Redes','iii',20000)
    docenteInvestigador2 = DocenteInvestigador('Mariano', 'Orellano', 5, 40000, 8, 'geofisica', 'geofisica general',
                                               'semiexclusivo', 'geofisica', 'gravimetria', 'i', 15000)
    docenteInvestigador3 = DocenteInvestigador('Josefina', 'Ruiz', 6, 55000, 12, 'geofisica', 'fisica 4', 'simple',
                                               'geofisica', 'electromagnetismo', 'iv', 25000)
    docenteInvestigador4 = DocenteInvestigador('Carlos', 'Ahumada', 7, 70000, 30, 'licenciatura en ciencias de la computacion',
                                               'analisis matematico 2', 'semiexclusivo', 'informatica', 'algoritmia', 'i', 18000)
    docenteInvestigador5 = DocenteInvestigador('Analia', 'Retamal', 8, 57000, 17, 'geofisica', 'geologia general', 'exclusivo',
                                               'geologia', 'rocas igneas', 'iv', 25000)
    lista_agentes = []
    lista_agentes.append(personalDeApoyo)
    lista_agentes.append(docente)
    lista_agentes.append(investigador)
    lista_agentes.append(docenteInvestigador)
    lista_agentes.append(docenteInvestigador2)
    lista_agentes.append(docenteInvestigador3)
    lista_agentes.append(docenteInvestigador4)
    lista_agentes.append(docenteInvestigador5)
    diccionario = listaToJSON(lista_agentes)
    del lista_agentes
    jsonF = objectEncoder()
    jsonF.guardarJSONArchivo(diccionario, 'personal.json')


if __name__ == '__main__':
    limpiarPantalla()
    test()
    personal = Lista()
    permisosAdmin = IPermisosAdmin(personal)
    permisosUsuario = IPermisosUsuario(personal)
    permisosUsuario.mostrarElementos()
    cargarDatosPersonal(permisosAdmin)
    menu = Menu()
    salir = False
    while not salir:
        mostrarMenu()
        op = int(input('Ingrese una opcion: '))
        limpiarPantalla()
        menu.opcion(op, permisosAdmin, permisosUsuario)
        salir = op == 0
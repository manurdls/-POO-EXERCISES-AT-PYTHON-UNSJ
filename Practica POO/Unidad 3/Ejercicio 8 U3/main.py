from limpiarPantalla import limpiarPantalla
import datetime
from datetime import date
#from datetime import datetime
from claseEmpleado import Empleado
from claseDePlanta import DePlanta
from claseContratado import Contratado
from claseExterno import Externo
from manejadorEmpleados import manejadorEmpleados
from claseMenu import Menu

def testEmpleados():
    empleadoDePlanta = DePlanta('38409657', 'Manuel Rossi', 'San Juan 785 - Jachal', '2644578712', 55000, 10)
    print(empleadoDePlanta)
    print('')
    empleadoContratado = Contratado('38409657', 'Manuel Rossi', 'San Juan 785 - Jachal', '2644578712',
                                    date.today(), date.today() + datetime.timedelta(days=90), 20)
    print(empleadoContratado)
    print('')
    empleadoExterno = Externo('38409657', 'Manuel Rossi', 'San Juan 785 - Jachal', '264578712',
                              date.today(), date.today() + datetime.timedelta(days=90), 'Carpinteria', 700, 15000, 2000)
    print(empleadoExterno)
if __name__ == '__main__':
    #testEmpleados()
    #fecha_str = "2020-05-22"
    #date_object = datetime.strptime(fecha_str, '%Y-%m-%d').date()
    #print(date_object)

    dim = -1
    while dim < 1:
        dim = int(input('Ingrese la dimension del arreglo: '))
        limpiarPantalla()
        if dim < 1:
            print('Error: la dimension debe ser mayor a cero.')
    empleados = manejadorEmpleados(dim)
    empleados.cargarDatos()

    menu = Menu()
    salir = False
    while not salir:
        print('\n---------MENU---------\n'
              '0. Salir\n'
              '1. Registrar horas\n'
              '2. Total de tarea\n'
              '3. Ayuda\n'
              '4. Calcular sueldo\n'
              '5. Acceder a funcionalidades de Tesorero/Gerente')
        op = int(input('Ingrese una opcion: '))
        limpiarPantalla()
        menu.opcion(op, empleados)
        salir = op==0
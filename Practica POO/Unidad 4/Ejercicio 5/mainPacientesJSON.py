
from clasePaciente import Paciente
from claseManejadorPacientes import ManejadorPacientes
from claseObjectEncoderPas import ObjectEncoder
def testPacientes(manejadorP):
    paciente1=Paciente('Rueda', 'Melisa', '(264)4777222', '160', '60')
    paciente2=Paciente('López', 'Carlos', '(261)4888111', '173', '95')
    paciente3=Paciente('Pérez', 'Maira', '(264)5111222', '172', '80')
    paciente4=Paciente('Altamirano', 'Sandra','(263)6478912', '164', '55')
    paciente5=Paciente('Artime', 'Luis', '(264)4558699', '186', '105')
    manejadorP.agregarPaciente(paciente1)
    manejadorP.agregarPaciente(paciente2)
    manejadorP.agregarPaciente(paciente3)
    manejadorP.agregarPaciente(paciente4)
    manejadorP.agregarPaciente(paciente5)



if __name__=='__main__':
    jF = ObjectEncoder('pacientes.json')
    manejador=ManejadorPacientes()
    testPacientes(manejador)

    diccionario=jF.leerJSONArchivo()
    manejador=jF.decodificarDiccionario(diccionario)
    manejador.mostrarPacientes()
    #diccionarioManejador=manejador.toJSON()
    #jF.guardarJSONArchivo(diccionarioManejador)
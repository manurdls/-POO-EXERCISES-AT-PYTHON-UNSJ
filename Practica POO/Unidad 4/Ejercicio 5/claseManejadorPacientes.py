from clasePaciente import Paciente

class ManejadorPacientes(object):
    indice = 0
    __pacientes = None

    def __init__(self):
        self.__pacientes=[]

    def mostrarPacientes(self):
        for i in self.__pacientes:
            print('Apellido: {}\nNombre: {}\nTelefono: {}\nAltura: {}\nPeso: {}\n'.format(i.getApellido(),
                                                                                          i.getNombre(),
                                                                                          i.getTelefono(),
                                                                                          i.getAltura(),
                                                                                          i.getPeso()))
    def agregarPaciente(self, paciente):
        paciente.rowid = ManejadorPacientes.indice
        self.__pacientes.append(paciente)
        ManejadorPacientes.indice += 1
    def getListaPacientes(self):
        return self.__pacientes
    def deletePaciente(self, paciente):
        indice = self.obtenerIndicePaciente(paciente)
        self.__pacientes.pop(indice)
    def updatePaciente(self, paciente):
        indice = self.obtenerIndicePaciente(paciente)
        self.__pacientes[indice] = paciente
    def obtenerIndicePaciente(self, paciente):
        bandera = False
        i = 0
        while not bandera and i < len(self.__pacientes):
            if self.__pacientes[i].rowid == paciente.rowid:
                bandera = True
            else:
                i += 1
        return i
    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            pacientes=[paciente.toJSON() for paciente in self.__pacientes]
        )
        return d


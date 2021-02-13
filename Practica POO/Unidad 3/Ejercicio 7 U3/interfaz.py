from zope.interface import Interface

class IPermisosAdmin(Interface):
    def insertarElemento(self, posicion, componente):
        pass

    def agregarElementoFin(self, componente):
        pass

class IPermisosUsuario(Interface):
    def mostrarElementos(self):
        pass

    def obtenerListadoDocentesInvestigadores_xCarrera(self, carrera):
        pass
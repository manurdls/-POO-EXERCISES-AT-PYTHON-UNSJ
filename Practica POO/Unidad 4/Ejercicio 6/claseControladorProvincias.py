from vistaProvincias import NewProvince
from claseManejadorProvincias import ManejadorProvincias


class ControladorProvincias(object):
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.provincias = list(repo.obtenerListaProvincias())

    def crearProvincia(self):
        nuevaProvincia = NewProvince(self.vista).show()
        if nuevaProvincia:
            provincia = self.repo.agregarProvincia(nuevaProvincia)
            del self.provincias
            self.provincias = list(self.repo.obtenerListaProvincias())
            self.vista.agregarProvincia(provincia)

    def seleccionarProvincia(self, index):
        self.seleccion = index
        provincia = self.provincias[index]
        self.repo.actualizarDatosProvincia(provincia)
        self.vista.verProvinciaEnForm(provincia)

    def start(self):
        for p in self.provincias:
            self.vista.agregarProvincia(p)
        self.vista.mainloop()
    def salirGrabarDatos(self):
        self.repo.grabarDatos()
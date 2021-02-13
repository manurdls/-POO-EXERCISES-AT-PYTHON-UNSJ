from claseRepositorioProvinciasJSON import RespositorioProvincias
from vistaProvincias import ProvincesView
from claseControladorProvincias import ControladorProvincias
from claseObjectEncoder import ObjectEncoder
def main():
    conn=ObjectEncoder('datos.json')
    repo=RespositorioProvincias(conn)
    vista=ProvincesView()
    ctrl=ControladorProvincias(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()
if __name__ == "__main__":
    main()
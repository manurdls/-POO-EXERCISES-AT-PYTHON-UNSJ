from claseRepositorioContactosJSON import RespositorioContactos
from vistaContactos import ContactsView
from claseControladorContactos import ControladorContactos
from claseObjectEncoder import ObjectEncoder
def main():
    conn=ObjectEncoder('contactos.json')
    repo=RespositorioContactos(conn)
    vista=ContactsView()
    ctrl=ControladorContactos(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()
if __name__ == "__main__":
    main()
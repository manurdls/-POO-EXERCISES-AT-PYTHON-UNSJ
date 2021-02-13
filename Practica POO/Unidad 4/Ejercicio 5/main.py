from claseRepositorioPacientesJSON import RespositorioPacientes
from vistaPacientes import PatientsView
from claseControladorPacientes import ControladorPacientes
from claseObjectEncoder import ObjectEncoder
def main():
    conn=ObjectEncoder('pacientes.json')
    repo=RespositorioPacientes(conn)
    vista=PatientsView()
    ctrl=ControladorPacientes(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()
if __name__ == "__main__":
    main()
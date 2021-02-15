from claseEmail import Email
import moduloVerificaciones

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.registroUsuario,
                            2:self.incisoB,
                            3:self.incisoC,
                         }
    def getSwitcher(self):
        return self.__switcher
    def option(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()

    ############### INICIO OPCIONES MENU ###############
    def salir(self):
        print("Fin programa")

    def registroUsuario(self):
        name = input("Ingrese su nombre: ")
        email = input("Ingrese su email: ")
        if moduloVerificaciones.verifSintaxEmail(email):
            emailInstance = Email(email)
            if not moduloVerificaciones.verifExistenciaEmail(email):
                emailInstance.setPassword(input("Ingrese su password: "))
                print("Estimado {}, su cuenta ha sido registrada exitosamente. Enviaremos un correo de autentificación"
                      "a la siguiente direccion: {}".format(name, emailInstance.__str__()))
            else:
                print("El email ya se encuentra en uso")
        else:
            print("Formato de mail incompatible")
    def incisoB(self):
        print('incisoB')


    def incisoC(self):
        print('incisoC')

    ############### FIN OPCIONES MENU ###############
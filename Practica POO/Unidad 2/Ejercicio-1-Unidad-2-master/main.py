import csv

from claseEmail import Email


if __name__ == '__main__':

    #inciso 1
    print('Ingrese los siguientes datos:')
    nombre = input('Nombre:')
    idCuenta = input('Id de la cuenta:')
    dominio = input('Dominio de la cuenta:')
    tipoDominio = input('Tipo de dominio de la cuenta:')
    contrasena = input('Contrasena:')
    mail = Email(idCuenta, dominio, tipoDominio, contrasena)
    #os.system('cls')
    print('Estimado {} te enviaremos tus mensajes a la dirección {}'.format(nombre, mail.__str__()))

    #inciso 2
    contrasena = input('Ingrese contraseña actual:')
    mail.modificarContrasena(contrasena)

    #inciso 3
    email = input('Ingrese un email: ')
    nuevoMail = Email()
    if nuevoMail.crearCuenta(email):
        print(nuevoMail)
    else:
        del nuevoMail

    #inciso 4
    direcciones = []
    dominio = input('Ingrese un dominio:')
    cont = 0
    archivo = open('archivo.csv')
    reader = csv.reader(archivo, delimiter=',')
    for fila in reader:
        direcciones.append(Email(fila[0], fila[1], fila[2], fila[3]))
    archivo.close()
    for i in range(len(direcciones)):
        if direcciones[i].getDominio() == dominio:
            cont += 1
    print('{} direcciones tienen igual dominio al ingresado.'.format(cont))

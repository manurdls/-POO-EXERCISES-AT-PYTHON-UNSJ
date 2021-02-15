import csv
import re

def verifSintaxEmail(email):
    ret = False
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', email.lower()):
        ret = True
    return ret

def verifExistenciaEmail(email):
    ret = False
    archivo = open('archivo.csv')
    reader = csv.reader(archivo, delimiter=',')
    for fila in reader:
        auxEmail = fila[0] + "@" + fila[1] + "." + fila[2]
        if (email.lower() == auxEmail.lower()):
            print(" {} {}".format(email, auxEmail))
            ret = True
    return ret

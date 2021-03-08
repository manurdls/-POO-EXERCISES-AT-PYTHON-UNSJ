

def main():
    mi_variable = 'uno, dos'
    print('Dirección de memoria: {}, Valor almacenado: {}'.format(hex(id(mi_variable)), mi_variable))
    mi_variable += 'tres'
    print('Dirección de memoria: {}, Valor almacenado: {}'.format(hex(id(mi_variable)), mi_variable))

    ##CUANDO EL VALOR DE UNA VARIABLE INMUTABLE CAMBIA, TAMBIÉN LO HACE LA DIRECCIÓN A LA QUE
    ##DICHA VARIABLE APUNTA.

if __name__ == '__main__':
    main()
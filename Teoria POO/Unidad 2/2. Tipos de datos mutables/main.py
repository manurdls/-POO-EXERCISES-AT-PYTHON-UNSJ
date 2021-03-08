
def mutable():
    mi_lista = [1,2,3,4,5]
    print('Dirección de memoria: {}, Valor almacenado: {}'.format(hex(id(mi_lista)), mi_lista))
    mi_lista[0] = 26
    mi_lista.append(27)
    print('Dirección de memoria: {}, Valor almacenado: {}'.format(hex(id(mi_lista)), mi_lista))

    ##LA DIRECCIÓN DE LA VARIABLE QUE ALMACENA UN TIPO DE DATO MUTABLE NO CAMBIA AUNQUE EL OBJETO CAMBIE.

if __name__ == '__main__':
    mutable()
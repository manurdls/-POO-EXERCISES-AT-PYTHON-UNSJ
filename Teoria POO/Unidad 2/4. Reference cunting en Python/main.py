
def ejemploRefcount():
    uno = 1
    dos = uno
    tres = uno
    cuatro = 1
    for k, v in locals().items():
        print('Dirección de {}: {}, Valor: {}'.format(k, hex(id(v)), v))

    ##TODAS LAS VARIABLES APUNTAN A LA MISMA UBICACIÓN DE MEMORIA, EL
    ##VALOR 1 SE ALMACENA UNA SOLA VEZ, Y CUALQUIER OTRA COSA QUE APUNTE A 1,
    ##HARÁ REFERENCIA A ESA UBICACIÓN DE MEMORIA.

if __name__ == '__main__':
    ejemploRefcount()
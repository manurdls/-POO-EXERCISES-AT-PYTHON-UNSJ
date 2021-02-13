from functools import partial
def ponerNumero(num):
    print(num)
def testAPP():
    ponerNumero(8)
    funcionParcial=partial(ponerNumero,5)
    funcionParcial()
    otraFuncionParcial=partial(ponerNumero,7)
    otraFuncionParcial()
if __name__ == '__main__':
    testAPP()

#parece que no pero esto es muy util cuando necesitamos llamar a funciones que admiten
#parámetro/s desde un parámetro(donde se llama a la funcion directamente sin los () )
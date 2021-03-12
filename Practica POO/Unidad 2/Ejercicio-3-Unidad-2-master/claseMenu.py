

class Menu(object):
    __switcher = None

    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.opc1,
                            2:self.opc2,
                            }

    def opcion(self, op, cosecha, camiones):
        func = self.__switcher.get(op, lambda: print('La opción no es válida'))
        if op == 0:
            func()
        else:
            if op == 1:
                func(cosecha)
            else:
                if op == 2:
                    func(cosecha, camiones)

    def salir(self):
        print('Fin Programa')
    def opc1(self, cosecha):
        id = int(input('Ingrese el id de un camión: '))
        print('Cantidad de total de kilos descargados: ',cosecha.getCantidadDeKilosDescargadosDeUnCamion(id))
    def opc2(self,cosecha,camiones):
        dia = int(input('Ingrese un dia: '))
        print('PATENTE          CONDUCTOR           CANTIDAD DE KILOS')
        for i in range(camiones.getCantCamiones()):
            camion = camiones.getCamion(i)
            print('%16s %20s %17s' % (camion.getPatente().ljust(16, " "),
                                      camion.getConductor().ljust(20, " "),
                                      str(cosecha.getCosechaEnUnDiaPorUnCamion(i+1,dia)).center(17, " ")))
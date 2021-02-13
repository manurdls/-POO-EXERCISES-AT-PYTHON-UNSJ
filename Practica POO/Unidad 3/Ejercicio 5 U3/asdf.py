def mostrarElemento(self, posicion):
    mensajeError = 'Error: posicion ingresada fuera de rango, la lista tiene {} componentes'.format(self.__tope)
    if self.__comienzo == None:
        print('Error: la lista está vacia')
    else:
        if posicion < self.__tope:
            aux = self.__comienzo
            i = 0
            while i < posicion and aux != None:
                aux = aux.getSiguiente()
                i += 1
            print('El dato es: ', aux.getDato())
        else:
            print(mensajeError)

    def insertarElemento(self, posicion, componente):
        retorno = False
        mensajeError = 'Error: posicion ingresada fuera de rango, la lista tiene {} componentes'.format(self.__tope)
        if posicion == 0:
            self.agregarElementoInicio(componente)
            retorno = True
        else:
            if self.__comienzo == None:
                print(mensajeError)
            else:
                i = 0
                aux = self.__comienzo
                while i < posicion and aux != None:
                    anterior = aux
                    aux = aux.getSiguiente()
                    i += 1
                if i == posicion and aux != None:
                    nuevoNodo = Nodo(componente)
                    nuevoNodo.setSiguiente(aux)
                    anterior.setSiguiente(nuevoNodo)
                    self.__tope += 1
                    print('El elemento se ha insertado correctamente')
                else:
                    print(mensajeError)
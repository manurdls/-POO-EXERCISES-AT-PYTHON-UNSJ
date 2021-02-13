from tkinter import *
from tkinter import ttk, messagebox
from functools import partial
from claseFraccion import Fraccion


class Calculadora(object):
    __ventana = None
    __operador = None
    __panel = None
    __primerOperando = None
    __segundoOperando = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        self.__ventana.geometry('+600+200')
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar(value='0')
        self.__operador = StringVar(value='')
        operatorEntry = ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(row=0, column=0, columnspan=1, sticky=(W, E))
        panelEntry = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right', state='disabled')
        panelEntry.grid(row=0, column=1, columnspan=2, sticky=(W, E))
        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(row=1, column=0, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO, '2')).grid(row=1, column=1, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO, '3')).grid(row=1, column=2, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO, '4')).grid(row=2, column=0, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO, '5')).grid(row=2, column=1, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO, '6')).grid(row=2, column=2, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO, '7')).grid(row=3, column=0, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO, '8')).grid(row=3, column=1, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO, '9')).grid(row=3, column=2, sticky=W)
        ttk.Button(mainframe, text='/', command=self.ponerBarra).grid(row=4, column=0, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(row=4, column=1, sticky=W)
        ttk.Button(mainframe, text='(-)', command=self.negarNumero).grid(row=4, column=2, sticky=W)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(row=5, column=0, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(row=5, column=1, sticky=W)
        ttk.Button(mainframe, text='AC', command=self.reiniciar).grid(row=5, column=2, sticky=W) #cambiar metodo
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(row=6, column=0, sticky=W)
        ttk.Button(mainframe, text='%', command=partial(self.ponerOPERADOR, '%')).grid(row=6, column=1, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(row=6, column=2, sticky=W)

        self.__bandDeCtrl = False

        self.__ventana.mainloop()
    def ponerNUMERO(self, numero):
        if self.__bandDeCtrl == True:
            self.__panel.set('0')
            self.__bandDeCtrl = False
        if self.__operador.get() == '':
            valor = self.__panel.get() + numero
            valor = self.changeTipo(valor)
            self.__primerOperando = valor
            valor = str(valor)
            self.__panel.set(valor)
            print('Primer operando: ',self.__primerOperando)
        else:
            valor = self.__panel.get() + numero
            valor = self.changeTipo(valor)
            self.__segundoOperando = valor
            valor = str(valor)
            self.__panel.set(valor)
            print('Segundo operando: ', self.__segundoOperando)


    def resolverOperacion(self, operando1, operacion, operando2):
        resultado = 0
        if operacion == '+':
            resultado = operando1 + operando2
        else:
            if operacion == '-':
                resultado = operando1 - operando2
            else:
                if operacion == '*':
                    resultado = operando1 * operando2
                else:
                    if operacion == '%':
                        resultado = operando1 // operando2
        print('Resultado: {}\nTipo: {}'.format(resultado, type(resultado)))
        if type(resultado) != Fraccion:
            resultado = self.changeTipo(str(resultado))
        return resultado

    def ponerOPERADOR(self, op):
        if op == '=':
            if self.__operador.get() != '':
                if self.__segundoOperando == None:
                    messagebox.showerror('ERROR', 'SintaxError')
                else:
                    resultado = self.resolverOperacion(self.__primerOperando,
                                                       self.__operador.get(),
                                                       self.__segundoOperando)
                    self.__primerOperando = resultado
                    self.__segundoOperando = None
                    self.__panel.set(str(resultado))
                    self.__operador.set('')
                    self.__bandDeCtrl = True
        else:
            if self.__operador.get() == '':
                self.__operador.set(op)
                self.__bandDeCtrl = True
            else:
                if self.__segundoOperando != None:
                    resultado = self.resolverOperacion(self.__primerOperando,
                                                       self.__operador.get(),
                                                       self.__segundoOperando)
                    self.__primerOperando = resultado
                    self.__segundoOperando = None
                    self.__panel.set(str(resultado))
                    self.__operador.set(op)
                    self.__bandDeCtrl = True
                else:
                    self.__operador.set(op)

    def changeTipo(self, cadena):
        i = cadena.find('/')
        if i != -1:
            numerador = cadena[0:i]
            denominador = cadena[i+1:len(cadena)]
            numerador = int(numerador)
            denominador = int(denominador)
            if denominador == 0:
                self.errorDivisionPorCero()
                resultado = 0
            else:
                resultado = Fraccion(numerador, denominador)
        else:
            i = cadena.find('.')
            if i != -1:
                resultado = float(cadena)
                cadena = cadena[i+1:len(cadena)]
                if int(cadena) == 0:
                    resultado = int(resultado)
            else:
                resultado = int(cadena)
        return resultado

    def reiniciar(self):
        self.__panel.set('0')
        self.__operador.set('')
        self.__primerOperando = None
        self.__segundoOperando = None

    def negarNumero(self):

        def buscarBarra(cadena):
            indexBarra = cadena.find('/')
            if indexBarra != -1:
                if indexBarra + 1 == len(cadena):
                    self.__panel.set(cadena + '-')
                else:
                    messagebox.showerror('ERROR', 'SintaxError')

        cadena = self.__panel.get()
        if cadena.find('-') == -1:
            if cadena == '0':
                self.__panel.set('-'+cadena)
            else:
                buscarBarra(cadena)
        else:
            buscarBarra(cadena)

    def ponerBarra(self):
        cadena = self.__panel.get()
        if cadena.find('/') == -1:
            self.__panel.set(cadena+'/')
        else:
            messagebox.showerror('ERROR', 'SintaxError')

    def errorDivisionPorCero(self):
        messagebox.showerror('ERROR', 'ZeroDivisionError')

def main():
    calculadora = Calculadora()

if __name__ == '__main__':
    main()
from tkinter import *
from tkinter import ttk
from functools import partial
from claseFraccion import Fraccion
import re


class Calculadora(object):
    __ventana = None
    __panel = None
    __operador = None
    __primerOperando = None
    __segundoOperando = None
    __bandDeCtrl = None
    __fraccionRegex = None
    __enteroRegex = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        self.__ventana.geometry('+600+200')
        self.__ventana.resizable(0,0)
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar(value='0')
        self.__operador = StringVar(value='')
        self.__enteroRegex = re.compile(r"^-?[0-9]+$")
        self.__fraccionRegex = re.compile(r"^-?[0-9]+/{1}-?[0-9]+$")
        operatorEntry = ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(row=0, column=0, columnspan=1, sticky=(W, E))
        panelEntry = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right', state='disabled')
        panelEntry.grid(row=0, column=1, columnspan=2, sticky=(W, E))
        ttk.Button(mainframe, text='1', command=partial(self.ponerCARACTER, '1')).grid(row=1, column=0, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerCARACTER, '2')).grid(row=1, column=1, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerCARACTER, '3')).grid(row=1, column=2, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerCARACTER, '4')).grid(row=2, column=0, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerCARACTER, '5')).grid(row=2, column=1, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerCARACTER, '6')).grid(row=2, column=2, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerCARACTER, '7')).grid(row=3, column=0, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerCARACTER, '8')).grid(row=3, column=1, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerCARACTER, '9')).grid(row=3, column=2, sticky=W)
        ttk.Button(mainframe, text='/', command=partial(self.ponerCARACTER, '/')).grid(row=4, column=0, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerCARACTER, '0')).grid(row=4, column=1, sticky=W)
        ttk.Button(mainframe, text='(-)', command=partial(self.ponerCARACTER, '-')).grid(row=4, column=2, sticky=W)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(row=5, column=0, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(row=5, column=1, sticky=W)
        ttk.Button(mainframe, text='AC', command=self.reiniciar).grid(row=5, column=2, sticky=W) #cambiar metodo
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(row=6, column=0, sticky=W)
        ttk.Button(mainframe, text='%', command=partial(self.ponerOPERADOR, '%')).grid(row=6, column=1, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(row=6, column=2, sticky=W)
        self.__bandDeCtrl = False
        self.__ventana.mainloop()

    def ponerCARACTER(self, caracter):
        if self.__bandDeCtrl == True:
            self.__panel.set('0')
            self.__bandDeCtrl = False
        valor = self.__panel.get()
        if valor == '0' and caracter != '/':
            valor = ''
        else:
            if valor == '-0' and caracter != '/':
                valor = '-'
        valor = valor + caracter
        self.__panel.set(valor)

    def changeTipo(self, valor):
        if self.__enteroRegex.match(valor) or self.__fraccionRegex.match(valor):
            i = valor.find('/')
            if i != -1:
                numerador = valor[0:i]
                denominador = valor[i+1:len(valor)]
                numerador = int(numerador)
                denominador = int(denominador)
                if denominador == 0:
                    resultado = 'Math ERROR'
                else:
                    resultado = Fraccion(numerador, denominador)
            else:
                valor = int(valor)
                resultado = Fraccion(valor)
        else:
            resultado = 'Syntax ERROR'
        return resultado

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
        return resultado

    def ponerOPERADOR(self, op):

        def resolver():
            self.__segundoOperando = valor
            resultado = self.resolverOperacion(self.__primerOperando,
                                               self.__operador.get(),
                                               self.__segundoOperando)
            if resultado == 'Math ERROR':
                self.error(resultado)
            else:
                self.__panel.set(str(resultado))
                self.__operador.set(op)
                self.__primerOperando = resultado
                self.__segundoOperando = None
                self.__bandDeCtrl = True

        if self.__operador.get() == '':
            self.__operador.set(op)
            self.ponerOPERADOR(op)
        else:
            valor = self.__panel.get()
            valor = self.changeTipo(valor)
            if valor == 'Math ERROR' or valor == 'Syntax ERROR':
                self.error(valor)
            else:
                if op == '=':
                    if self.__primerOperando == None:
                        self.__primerOperando = valor
                        self.__panel.set(str(valor))
                        self.__bandDeCtrl = True
                    else:
                        if self.__operador.get() == '=':
                            pass
                        else:
                            resolver()
                else:
                    if self.__operador.get() == '=':
                        self.__primerOperando = valor
                        self.__operador.set(op)
                        self.__bandDeCtrl = True
                    else:
                        if self.__primerOperando == None:
                            self.__primerOperando = valor
                            self.__operador.set(op)
                            self.__bandDeCtrl = True
                        else:
                            resolver()

    def reiniciar(self):
        self.__panel.set('0')
        self.__operador.set('')
        self.__primerOperando = None
        self.__segundoOperando = None

    def error(self, error):
        self.reiniciar()
        self.__panel.set(error)
        self.__bandDeCtrl = True
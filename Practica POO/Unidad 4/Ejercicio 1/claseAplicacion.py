import tkinter as tk
from tkinter import *
from tkinter import ttk, font, messagebox


class Aplicacion(tk.Tk):
    __altura = None
    __peso = None
    __texto = None
    __texto2 = None

    def __init__(self):
        super().__init__()
        self.title('Calculadora de IMC')
        self.resizable(0,0)
        self.geometry('500x255+500+150')

        self.__altura = IntVar()
        self.__peso = IntVar()
        self.__texto = StringVar()
        self.__texto.set('')
        self.__texto2 = StringVar()
        self.__texto2.set('')

        opts = {'ipadx': 10, 'ipady': 5, 'sticky': 'nswe'}
        fuente = font.Font(font='Verdana 10 bold')
        fuente2 = font.Font(family='Helvetica', size=20)

        #UNICO FRAME DE LA VENTANA
        frame1 = ttk.Frame(self, relief='sunken').grid()

        #TITULO
        tk.Label(frame1, text='Calculadora de IMC', font=fuente2).grid(row=0, column=0, columnspan=4, sticky='n', ipady=15)
        ttk.Separator(frame1, orient=HORIZONTAL).grid(row=1, column=0, columnspan=4, sticky='nswe', pady=5)

        #LABEL DE PESO Y ALTURA
        ttk.Label(frame1, text='Altura:', foreground='grey').grid(row=2, column=0, **opts)
        ttk.Label(frame1, text='Peso:', foreground='grey').grid(row=3, column=0, **opts, pady=5)

        #ENTRY DE PESO Y ALTURA
        self.entryAltura = ttk.Entry(frame1, textvariable = self.__altura, width=44)
        self.entryAltura.grid(row=2, column=1, columnspan=2, **opts)
        self.entryAltura.bind(sequence='<Return>', func= self.eventoEnterCalcular)
        self.entryPeso = ttk.Entry(frame1, textvariable=self.__peso, width=44)
        self.entryPeso.grid(row=3, column=1, columnspan=2, **opts, pady=5)
        self.entryPeso.bind(sequence='<Return>', func=self.eventoEnterCalcular)

        #LABEL DE cm y kg
        tk.Label(frame1, text='cm', bg='grey').grid(row=2, column=3, **opts)
        tk.Label(frame1, text='kg', bg='grey', padx=3).grid(row=3, column=3, **opts, pady=5)
        ttk.Separator(frame1, orient=HORIZONTAL).grid(row=4, column=0, columnspan=4, sticky='nswe')

        #BOTONES CALCULAR Y LIMPIAR
        self.botonCalcular = tk.Button(frame1, text='Calcular', command=self.calcular, bg='green', fg='white', font=fuente)
        #style = ttk.Style()
        #style.configure("TButton", background='green', foreground='white', font=fuente)
        #self.botonCalcular = ttk.Button(frame1, text='Calcular',underline=0,command=self.calcular)
        self.botonCalcular.grid(row=5, column=1, **opts, pady=5)
        self.botonCalcular.bind(sequence='<Return>', func=self.eventoEnterCalcular)
        self.botonLimpiar = tk.Button(frame1, text='Limpiar', command=self.limpiar, background='green', fg='white', font=fuente)
        self.botonLimpiar.grid(row=5, column=2, **opts, pady =5)
        self.botonLimpiar.bind(sequence='<Return>', func=self.eventoEnterLimpiar)

        #LABEL DE SALIDA
        ttk.Label(frame1, textvariable=self.__texto, foreground='green').grid(row=6, column= 0, columnspan=4, pady=5)
        ttk.Label(frame1, textvariable=self.__texto2, foreground='green', font=fuente).grid(row=7, column=0, columnspan=4)

        self.mainloop()

    def calcular(self):
        try:
            altura = self.__altura.get()
            peso = self.__peso.get()
            assert altura > 0, ''
            assert peso > 0, ''

        except:
            messagebox.showerror(title='ERROR', message='Datos incorrectos')
            self.limpiar()
        else:
            altura = altura/100
            imc = round(peso / (altura*altura), 1)
            texto = 'Tu Indice de Masa Corporal (IMC) es '+str(imc)+' Kg/m2'
            self.__texto.set(texto)
            self.devolucionIMC(imc)
            self.botonLimpiar.focus()

    def devolucionIMC(self, imc):
        if imc < 18.5:
            self.__texto2.set('Peso inferior al normal')
        else:
            if imc >= 18.5 and imc < 25.0:
                self.__texto2.set('Normal')
            else:
                if imc >= 25.0 and imc < 30.0:
                    self.__texto2.set('Peso superior al normal')
                else:
                    if imc >= 30:
                        self.__texto2.set('Obesidad')

    def limpiar(self):
        self.__peso.set(0)
        self.__altura.set(0)
        self.__texto.set('')
        self.__texto2.set('')
        self.entryAltura.focus_set()

    def eventoEnterCalcular(self, event):
        self.calcular()

    def eventoEnterLimpiar(self, event):
        self.limpiar()
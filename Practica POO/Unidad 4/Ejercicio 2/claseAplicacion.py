from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox



class Aplicacion(tk.Tk):
    def __init__(self, dolarVenta):
        super().__init__()

        self.title('Conversor de moneda')
        #self.geometry('320x130+500+150')
        self.resizable(1,1)
        self.framePrincipal = FramePrincipal(self, dolarVenta)

    def cerrarAplicacion(self):
        self.destroy()

class FramePrincipal(ttk.Frame):
    __dolar = None
    __pesos = None
    __dolarVenta = None
    def __init__(self, master, dolarVenta):
        super().__init__(master, borderwidth=3, relief='sunken', padding=(10, 10))
        self.grid(row=0, column=0, sticky=(N, W, E, S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.__dolarVenta = dolarVenta
        self.__dolar = StringVar(value=0)
        self.__dolar.trace(mode='w', callback=self.calcularPesos)
        self.__pesos = StringVar()

        # ENTRY cifra en dólares
        self.entryDolar = ttk.Entry(self, textvariable=self.__dolar, width=10, justify='center')
        self.entryDolar.grid(row=0, column=1)
        self.entryDolar.select_range(0, len(self.__dolar.get()))
        self.entryDolar.focus()

        # Label dólares
        ttk.Label(self, text='dólares').grid(row=0, column=2)

        # Label es equivalente a
        ttk.Label(self, text='es equivalente a:').grid(row=1, column=0)

        # Label pesos
        ttk.Label(self, text='pesos').grid(row=1, column=2)

        # Boton salir
        self.boton = ttk.Button(self, text='Salir', command=quit)
        self.boton.grid(row=2, column=2)
        self.boton.bind(sequence='<Return>', func=lambda event: master.cerrarAplicacion())

        # Label pesos
        ttk.Label(self, textvariable=self.__pesos).grid(row=1, column=1)

    def calcularPesos(self, *args):
        if self.__dolar.get() != '':
            try:
                dolar = float(self.__dolar.get())
            except:
                messagebox.showerror(title='ERROR', message='Entrada errónea')
                self.__dolar.set(0)
                self.entryDolar.focus()
                self.entryDolar.select_range(0, len(self.__dolar.get()))
                self.__pesos.set('')
            else:
                pesos = round(dolar*self.__dolarVenta, 2)
                self.__pesos.set(pesos)
        else:
            self.__pesos.set('')
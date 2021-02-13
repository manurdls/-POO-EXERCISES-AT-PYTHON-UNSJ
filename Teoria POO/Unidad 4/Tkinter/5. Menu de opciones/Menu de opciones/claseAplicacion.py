import tkinter as tk
from tkinter import *
from tkinter import ttk, font

class App(tk.Tk):
    __version = 'Version 1.0'
    def __init__(self):
        super().__init__()

        self.fuente = font.Font(weight='normal')

        #creo la barra de menú
        barraMenu = Menu(self)
        #barraMenu = tk.Menu()

        #creo los sub menús
        menuArchivo = Menu(barraMenu, tearoff=1)
        menuAyuda = Menu(barraMenu, tearoff=1)
        menuSalir = Menu(barraMenu, tearoff=1)

        #configuro sub menú Archivo
        menuArchivo.add_command(label='Nuevo', command=self.nuevo, accelerator='Ctrl+n')
        menuArchivo.add_command(label='Abrir', command=self.abrir, accelerator='Ctrl+a')
        menuArchivo.add_separator()
        menuArchivo.add_command(label='Guardar')
        menuArchivo.add_command(label='Guardar como...')

        #configuro sub menú Ayuda
        menuAyuda.add_command(label='Acerca de...', command=self.acercaDe)

        #configuro sub menú Salir
        menuSalir.add_command(label='Salir', command=self.destroy)

        #agrego los sub menús a la barra de menú
        barraMenu.add_cascade(label='Archivo', menu=menuArchivo)
        barraMenu.add_cascade(label='Ayuda', menu=menuAyuda)
        barraMenu.add_cascade(label='Salir', menu=menuSalir)

        #agrego la barra de menú a la ventana principal
        self.config(menu=barraMenu)

        # eventos
        self.bind("<Control-n>",                        #esto sirve para enlazar eventos con combinaciónes de teclas
                  lambda event: self.nuevo())
        self.bind("<Control-a>",
                  lambda event: self.abrir())
        self.bind("<Control-q>",
                  lambda event: self.destroy())
        self.bind()

    def nuevo(self):
        print('Nuevo')
    def abrir(self):
        print('Abrir')
    def acercaDe(self):
        acerca = Toplevel()
        acerca.geometry('300x200')
        acerca.resizable(width=False, height=False)
        acerca.title('Acerca de')

        marco1 = ttk.Frame(acerca, padding=(10, 10, 10, 10), relief=RAISED)
        marco1.pack(side=TOP, fill=BOTH, expand=True)

        etiq2 = ttk.Label(marco1, text='APP-Menú '+self.__version, foreground='blue', font=self.fuente)
        etiq2.pack(side=TOP, padx=10)

        etiq3 = ttk.Label(marco1, text='Mi Primera App Con Menú')
        etiq3.pack(side=TOP, padx=10)

        boton1 = ttk.Button(marco1, text='Salir', command=acerca.destroy)
        boton1.pack(side=BOTTOM, padx=10, pady=10)

        boton1.focus_set()
        acerca.transient(self)
        self.wait_window(acerca)
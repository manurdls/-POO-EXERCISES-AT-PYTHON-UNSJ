from tkinter import *
from tkinter import ttk, messagebox
class Aplicacion():
    __ventana=None
    __pulgadas=None
    __centimetros=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('290x115')
        self.__ventana.title('Conversor Pulgadas a Centímetros')
        mainframe = ttk.Frame(self.__ventana, padding="5 5 12 5")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__pulgadas = StringVar()
        self.__centimetros = StringVar()
        self.__pulgadas.trace('w', self.calcular)       #ACÁ ESTÁ LA CLAVE
                                                        #se define una traza con la variable de entrada para detectar
                                                        #cambios en los datos ingresados. Si se producen cambios se
                                                        #llama a la función 'self.calcular' para validación y para
                                                        #calcular el equivalente a centimetros de las pulgadas ingresadas

        self.pulgadasEntry = ttk.Entry(mainframe, width=7, textvariable=self.__pulgadas)
        self.pulgadasEntry.grid(column=2, row=1, sticky=(W, E))
        ttk.Label(mainframe, textvariable=self.__centimetros).grid(column=2, row=2, sticky=(W, E))
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=3, row=3, sticky=W)
        ttk.Label(mainframe, text="pulgadas").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="es equivalente a").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="centímetros").grid(column=3, row=2, sticky=W)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.pulgadasEntry.focus()
        self.__ventana.mainloop()
    def calcular(self, *args):
        if self.pulgadasEntry.get()!='':
            try:
                valor=float(self.pulgadasEntry.get())   # VALIDA Y POSTERIORMENTE CALCULA
                self.__centimetros.set(2.54*valor)
            except ValueError:
                messagebox.showerror(title='Error de tipo',
                                     message='Debe ingresar un valor numérico')
                self.__pulgadas.set('')
                self.pulgadasEntry.focus()
        else:
            self.__centimetros.set('')
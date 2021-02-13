from tkinter import *
from tkinter import ttk, messagebox

class Aplicacion(object):
    __ventana = None
    __pulgadas = None
    __centimetros = None

    def __init__(self):
        self.__ventana = Tk()
        #self.__ventana.geometry(newGeometry='290x115')
        self.__ventana.title(string='Conversor Pulgadas a Centimetros')
        self.__ventana.configure(bg='red')

        mainframe = ttk.Frame(self.__ventana, padding="1 1 1 1", borderwidth=3, relief='sunken')  # W , N , E , S
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        self.__centimetros = StringVar()
        self.__pulgadas = StringVar()

        self.pulgadasEntry = ttk.Entry(master=mainframe, width=7, textvariable=self.__pulgadas)
        self.pulgadasEntry.grid(column=2, row=1, sticky=(W, E))

        #self.__centimetros.set('ola')
        ttk.Label(mainframe, textvariable=self.__centimetros).grid(column=2, row=2, sticky=(W, E))

        ttk.Button(mainframe, text="Calcular", command=self.calcular).grid(column=2, row=3, sticky=W) ##acá esta el llamado
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="pulgadas").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="es equivalente a").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="centímetros").grid(column=3, row=2, sticky=W)
        print(mainframe.winfo_children())

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.pulgadasEntry.focus()
        self.__ventana.mainloop()

    def calcular(self):
        try:
            valor = float(self.pulgadasEntry.get())     ## obtengo el dato
            self.__centimetros.set(2.54 * valor)        ## se ve claramente cómo calcula despues de obtener el dato
        except ValueError:
            messagebox.showerror(title='Error de tipo',
                             message='Debe ingresar un valor numérico')
            self.__pulgadas.set('')
            self.pulgadasEntry.focus()

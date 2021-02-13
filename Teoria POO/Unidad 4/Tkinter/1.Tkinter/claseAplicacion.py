from tkinter import *
from tkinter import ttk

class Aplicacion(object):
    def __init__(self):
        ventana = Tk()
        ventana.geometry(newGeometry='600x200')
        ventana.configure(bg='blue')
        ventana.title(string = 'FLOR TE AMO')
        ttk.Button()
        boton = ttk.Button(master=ventana, text='Salir', command=ventana.destroy)
        boton.pack(side=BOTTOM)
        ventana.mainloop()
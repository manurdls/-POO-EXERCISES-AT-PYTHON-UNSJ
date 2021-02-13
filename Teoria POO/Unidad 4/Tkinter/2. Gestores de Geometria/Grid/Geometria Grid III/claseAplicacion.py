from tkinter import *
from tkinter import ttk, font

class Aplicacion():
    __ventana = None
    __usuario = None
    __clave = None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Acceso')
        self.__ventana.resizable(0,0)

        self.marco =ttk.Frame(self.__ventana, borderwidth=5, relief='raised', padding=(10,10))
        self.marco.grid(row=0, column=0)

        fuente = font.Font(weight='bold')
        self.usuarioLbl = ttk.Label(self.marco, text='Usuario', font=fuente, padding=(5,5))
        self.contraseniaLbl = ttk.Label(self.marco, text='Contraseña', font=fuente, padding=(5, 5))

        self.__usuario = StringVar()
        self.__clave = StringVar()
        self.__usuario.set('')
        self.ctext1 = ttk.Entry(self.marco, textvariable=self.__usuario, width=30)
        self.ctext2 = ttk.Entry(self.marco, textvariable=self.__clave, width=30, show='*')

        self.separ = ttk.Separator(self.marco, orient=HORIZONTAL)

        self.boton1 = ttk.Button(self.marco, text='Aceptar', padding=(5, 5), command=self.aceptar)
        self.boton2 = ttk.Button(self.marco, text='Cancelar', padding=(5, 5), command=quit)

        #ahora hay que ubicar los widgets ya creados con Grid
        self.usuarioLbl.grid(row=0, column=0)
        self.ctext1.grid(row=0, column=1, columnspan=2)
        self.contraseniaLbl.grid(row=1, column=0)
        self.ctext2.grid(row=1, column=1, columnspan=2)
        self.separ.grid(row=2, column=0, columnspan=3)
        self.boton1.grid(row=3, column=1)
        self.boton2.grid(row=3, column=2)
        self.ctext1.focus_set()

        self.__ventana.mainloop()

    def aceptar(self):
        if self.__clave.get() == 'tkinter':
            print('Acceso permitido')
            print('Usuario: ',self.__usuario.get())
            print('Contraseña: ',self.__clave.get())
        else:
            print('Acceso denegado')
            self.__clave.set('')
            self.ctext2.focus_set()
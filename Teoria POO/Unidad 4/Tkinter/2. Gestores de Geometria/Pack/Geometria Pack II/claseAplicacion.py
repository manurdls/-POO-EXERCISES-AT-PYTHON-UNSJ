from tkinter import *
from tkinter import ttk, font

class Aplicacion():
    __ventana = None
    __clave = None
    __usuario = None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Acceso')

        fuente = font.Font(weight='bold')
        self.usuarioLbl = ttk.Label(self.__ventana, text='Usuario', font=fuente)
        self.contraseniaLbl = ttk.Label(self.__ventana, text='Contraseña', font=fuente)

        self.__usuario = StringVar()
        self.__clave = StringVar()
        #self.__usuario.set('')

        self.ctext1 = ttk.Entry(self.__ventana, textvariable=self.__usuario, width=30)
        self.ctext2 = ttk.Entry(self.__ventana, textvariable=self.__clave, width=30, show='*')

        self.separ1 = ttk.Separator(self.__ventana, orient=HORIZONTAL)

        self.boton1 = ttk.Button(self.__ventana, text='Aceptar', command=self.aceptar)
        self.boton2 = ttk.Button(self.__ventana, text='Cancelar', command=quit)

        #ahora solo queda ubicar los widgets ya creados con el gestor Pack
        self.usuarioLbl.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.ctext1.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.contraseniaLbl.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.ctext2.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.separ1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton1.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.boton2.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)
        self.ctext2.focus_set()

        self.__ventana.mainloop()

    def aceptar(self):
        if self.__clave.get() == 'tkinter':
            print('Acceso permitido')
            print('Usuario: ', self.ctext1.get())
            print('Contraseña: ', self.ctext2.get())
        else:
            print('Acceso denegado')
            self.__clave.set('')
            self.ctext2.focus_set()

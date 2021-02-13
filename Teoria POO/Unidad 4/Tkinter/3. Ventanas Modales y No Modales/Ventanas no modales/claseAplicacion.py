from tkinter import *
from tkinter import ttk

class Aplicacion():
    #variables de clase
    ventana = 0
    posx_y = 0
    #variables de instancia
    __ventanaPrincipal = None
    __dialogo = None

    def __init__(self):
        self.__ventanaPrincipal = Tk()
        self.__ventanaPrincipal.geometry('300x200+500+50')
        self.__ventanaPrincipal.resizable(0,0)
        self.__ventanaPrincipal.title('Ventana de aplicación')


        boton = ttk.Button(self.__ventanaPrincipal, text='Abrir', command=self.abrir)
        boton.pack(side=BOTTOM, padx=20, pady=20)

        self.__ventanaPrincipal.mainloop()

    def abrir(self):
        Aplicacion.ventana += 1
        Aplicacion.posx_y += 50
        tamypos = '200x100+'+str(Aplicacion.posx_y)+'+'+str(Aplicacion.posx_y)
        self.__dialogo = Toplevel()
        self.__dialogo.geometry(tamypos)
        self.__dialogo.resizable(0,0)
        ident = self.__dialogo.winfo_id()
        titulo = str(Aplicacion.ventana)+':'+str(ident)
        self.__dialogo.title(titulo)

        boton = ttk.Button(self.__dialogo, text='Salir', command=self.__dialogo.destroy)
        boton.pack(side=BOTTOM, padx=20, pady=20)

        self.__dialogo.transient(master=self.__ventanaPrincipal)
        self.__dialogo.grab_set()
        self.__ventanaPrincipal.wait_window(self.__dialogo)
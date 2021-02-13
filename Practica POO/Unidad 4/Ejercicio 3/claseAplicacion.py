from tkinter import *
from tkinter import ttk, font
import tkinter as tk
import requests
from datetime import datetime

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Cotización dolar')
        self.resizable(0, 0)
        self.geometry('+500+150')

        self.frame1 = Frame1(self)

        self.frame1.grid(row=0, column=0, sticky=(N, W, E, S))
        self.frame1.columnconfigure(0, weight=1)
        self.frame1.rowconfigure(0, weight=1)

class Frame1(ttk.Frame):
    __lista_dolar = None
    __ultima_actualizacion = None
    __test = 0  #sirve para probar que los datos se actualizan al darle al boton Actualizar
    def __init__(self, master):
        super().__init__(master=master, borderwidth=3, relief='sunken', padding=(3, 3, 3, 3))

        self.__ultima_actualizacion = StringVar(value='')
        self.__lista_dolar = self.getDatosApi()     #la lista contiene variables de control

        fuente = font.Font(font='Verdana 10 underline')
        self.lblTipoDolar = ttk.Label(self, text='Tipo de Dolar', width=20, font=fuente, anchor=tk.W)
        self.lblCompra = ttk.Label(self, text='Compra', width=15, font=fuente, anchor=tk.N)
        self.lblVenta = ttk.Label(self, text='Venta', width=15, font=fuente, anchor=tk.N)
        self.separador1 = ttk.Separator(self, orient=HORIZONTAL)
        self.separador2 = ttk.Separator(self, orient=HORIZONTAL)
        self.separador3 = ttk.Separator(self, orient=HORIZONTAL)

        row = 2
        for i in range(len(self.__lista_dolar)):
            ttk.Label(self, textvariable=self.__lista_dolar[i][0], width=20, relief='sunken').grid(row=row,
                                                                                                   column=0,
                                                                                                   columnspan=2)
            ttk.Label(self, textvariable=self.__lista_dolar[i][1], width=15, anchor=tk.N, relief='sunken').grid(row=row,
                                                                                                                column=2,
                                                                                                                columnspan=2)
            ttk.Label(self, textvariable=self.__lista_dolar[i][2], width=15, anchor=tk.N, relief='sunken').grid(row=row,
                                                                                                                column=4,
                                                                                                                columnspan=2)
            row += 1


        self.btnActualizar = ttk.Button(self, text='Actualizar', command=self.actualizarDatos, width=9)
        self.btnActualizar.bind('<Return>', lambda event: self.actualizarDatos())
        self.btnActualizar.focus()
        self.btnSalir = ttk.Button(self, text='Salir', command=master.quit, width=9)
        self.btnSalir.bind('<Return>', lambda event: master.quit())
        self.lblHoraModif = ttk.Label(self, textvariable=self.__ultima_actualizacion, foreground='green', anchor=tk.N)

        #disposición espacial de los widgets
        self.lblTipoDolar.grid(row=0, column=0, columnspan=2)
        self.lblCompra.grid(row=0, column=2, columnspan=2)
        self.lblVenta.grid(row=0, column=4, columnspan=2)
        self.separador1.grid(row=1, column=0, columnspan=6, sticky=tk.EW, pady=3)


        self.separador3.grid(row=row, column=0, columnspan=6, sticky=tk.EW, pady=3)
        row += 1
        self.lblHoraModif.grid(row=row, column=0, columnspan=6)
        row += 1
        self.separador2.grid(row=row, column=0, columnspan=6, sticky=tk.EW, pady=3)
        row += 1
        self.btnActualizar.grid(row=row, column=0, columnspan=3, sticky=tk.N)
        self.btnSalir.grid(row=row, column=3, columnspan=3, sticky=tk.N)

    def getDatosApi(self):
        #self.__test += 1   #descomentar para testear
        complete_url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        r = requests.get(complete_url)
        json = r.json()
        # print(json)
        lista_dolar = []
        for i in range(len(json)):
            nombre = json[i]['casa']['nombre']
            if nombre.lower().find('dolar') != -1:
                try:
                    compra = float(json[i]['casa']['compra'].replace(',', '.'))  # si se puede hacer el cast a float
                    venta = float(json[i]['casa']['venta'].replace(',', '.'))    # es porque existe un valor
                except:
                    pass
                else:
                    lista_dolar.append([StringVar(value=nombre),            #comentar para testear
                                        StringVar(value=compra),            #comentar para testear
                                        StringVar(value=venta)])            #comentar para testear
                    #lista_dolar.append([StringVar(value=str(self.__test)),     #descomentar para testear
                    #                    StringVar(value=str(self.__test)),     #descomentar para testear
                    #                    StringVar(value=str(self.__test))])    #descomentar para testear
        self.setUltmaActualizacion()
        return lista_dolar

    def setUltmaActualizacion(self):
        now = datetime.now()
        self.__ultima_actualizacion.set('Ulima actualización: '+
                                        str(now.day)+'/'+
                                        str(now.month)+'/'+
                                        str(now.year)+', '+
                                        str(now.hour)+':'+
                                        str(now.minute)+'hs')

    def actualizarDatos(self, *args):
        nueva_lista = self.getDatosApi()
        for i in range(len(nueva_lista)):
            for j in range(len(nueva_lista[i])):
                if self.__lista_dolar[i][j] != nueva_lista[i][j]:
                    self.__lista_dolar[i][j].set(nueva_lista[i][j].get())
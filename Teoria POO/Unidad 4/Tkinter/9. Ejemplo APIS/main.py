from tkinter import ttk,Tk,StringVar
from tkinter.constants import *
import requests

class Aplicacion():
    __ventana=None
    __respuestaEj2=None
    __respuestaEj3=None
    __respuestaEj6=None
    __ciudad=None
    __apikey=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('640x480')
        self.__ventana.title('Peticiones a APIs')
        mainframe = ttk.Frame(self.__ventana, padding="5 5 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__respuestaEj2 = StringVar()
        self.__respuestaEj3 = StringVar()
        self.__respuestaEj6 = StringVar()
        self.__ciudad = StringVar()
        self.__apikey = StringVar()
        ttk.Button(mainframe, text='Ejercicio 2', command=self.ej2).grid(column=0, row=0, sticky=W)
        ttk.Entry(mainframe, textvariable=self.__respuestaEj2).grid(column=1, row=0, sticky=W)
        ttk.Separator(mainframe, orient=HORIZONTAL).grid(row=1, column=0, columnspan=2, sticky=W, pady=5, ipadx=120)
        ttk.Button(mainframe, text='Ejercicio 3', command=self.ej3).grid(column=0, row=2, sticky=W)
        ttk.Entry(mainframe, textvariable=self.__respuestaEj3).grid(column=1, row=2, sticky=W)
        ttk.Separator(mainframe, orient=HORIZONTAL).grid(row=3, column=0, columnspan=2, sticky=W, pady=5, ipadx=120)
        ttk.Label(mainframe, text='Ejercicio 6').grid(column=0, row=4, sticky=W)
        ttk.Label(mainframe, text='Ciudad:').grid(column=0, row=5, sticky=W)
        ttk.Entry(mainframe, textvariable=self.__ciudad).grid(column=1, row=5, sticky=W)
        ttk.Label(mainframe, text='Api key:').grid(column=0, row=6, sticky=W)
        ttk.Entry(mainframe, textvariable=self.__apikey).grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, text='Solicitar', command=self.ej6).grid(column=0, row=7, sticky=W)
        ttk.Entry(mainframe, textvariable=self.__respuestaEj6).grid(column=1, row=7, sticky=W)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
            self.__ventana.mainloop()

    def ej2(self, *args):
        complete_url = 'https://www.dolarsi.com/api/api.php?type=dolar'
        r = requests.get(complete_url)
        print(r)
        self.__respuestaEj2.set(r.json())

    def ej3(self, *args):
        complete_url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        r = requests.get(complete_url)
        self.__respuestaEj3.set(r.json())

    def ej6(self, *args):
        complete_url = 'https://api.openweathermap.org/data/2.5/weather?q='+self.__ciudad.get()+'&units=metric&appid='+self.__apikey.get()
        r = requests.get(complete_url)
        self.__respuestaEj6.set(r.json())

def testAPP():
    mi_app = Aplicacion()

if __name__ == '__main__':
    testAPP()
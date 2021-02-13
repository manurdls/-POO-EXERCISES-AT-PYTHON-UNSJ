import tkinter as tk
from tkinter import messagebox
from claseProvincia import Provincia

class ProvincesView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Lista de provincias')
        self.list = ProvinceList(self, height=15)
        self.form = ExtendProvinceForm(self)
        self.btn = tk.Button(self, text='Agregar provincia')

        self.list.grid(row=0, column=0, rowspan=2, padx=3, pady=3)
        self.form.grid(row=0, column=1, columnspan=3, padx=3, pady=3)
        self.btn.grid(row=1, column=2, pady=10)
    def setControlador(self, ctrl):
        self.btn.config(command=ctrl.crearProvincia)
        self.list.bind_doble_click(ctrl.seleccionarProvincia)

    def agregarProvincia(self, provincia):
        self.list.insertar(provincia)

    def verProvinciaEnForm(self, provincia):
        self.form.mostrarEstadoProvinciaEnFormulario(provincia)

class ProvinceList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

    def insertar(self, provincia):
        index = provincia.rowid
        text = provincia.getNombre()
        self.lb.insert(index, text)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)

class NewProvince(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.provincia = None
        self.form = BasicProvinceForm(self)
        self.btn = tk.Button(self, text='Confirmar', command=self.confirmar)

        self.form.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.btn.grid(row=1, column=1, pady=10)

    def confirmar(self):
        self.provincia = self.form.crearProvinciaDesdeFormulario()
        if self.provincia:
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.provincia

class BasicProvinceForm(tk.LabelFrame):
    __fields = None
    def __init__(self, master, fields=None, **kwargs):
        super().__init__(master, text="Provincia", padx=10, pady=10, **kwargs)
        if fields == None:
            fields = ['Nombre', 'Capital', 'Cantidad de habitantes', 'Cantidad de departamentos/partidos']
        self.__fields = fields
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.__fields)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=40)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry

    def crearProvinciaDesdeFormulario(self):
        values = [e.get() for e in self.entries]
        provincia=None
        try:
            provincia = Provincia(*values)
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e), parent=self)
        return provincia

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)

class ExtendProvinceForm(BasicProvinceForm):
    __fields = ['Nombre', 'Capital', 'Cantidad de habitantes', 'Cantidad de departamentos/partidos',
                'Temperatura', 'Sensación térmica', 'Humedad']
    def __init__(self, master, **kwargs):
        super().__init__(master, self.__fields, **kwargs)

    def mostrarEstadoProvinciaEnFormulario(self, provincia):
        values = (provincia.getNombre(), provincia.getCapital(),
                  provincia.getCantHabitantes(), provincia.getCantDP(),
                  provincia.getTemperatura(), provincia.getSensacionTermica(), provincia.getHumedad())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
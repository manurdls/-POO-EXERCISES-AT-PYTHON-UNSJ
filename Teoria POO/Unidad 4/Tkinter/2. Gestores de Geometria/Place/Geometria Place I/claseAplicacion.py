import tkinter as tk

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        label_a = tk.Label(self, text='Label A', bg='yellow')
        label_b = tk.Label(self, text='Label B', bg='orange')
        label_c = tk.Label(self, text='Label C', bg='red')
        label_d = tk.Label(self, text='Label D', bg='green')
        label_e = tk.Label(self, text='Label E', bg='blue')

        label_a.place(relwidth=0.25, relheight=0.25)
        label_b.place(x=100, anchor=tk.N, width=100, height=50)
        label_c.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.5, relheight=0.5)
        label_c.place(relx=0.5, rely=0.5, anchor=tk.CENTER, relwidth=0.5, relheight=0.5)
        label_e.place(x=200, y=200, anchor=tk.S + tk.E, relwidth=0.25, relheight=0.25)
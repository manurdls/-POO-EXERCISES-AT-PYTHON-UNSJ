import tkinter as tk

class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pack Geometry")
        label_a = tk.Label(self, text='Label A', bg='yellow')
        label_b = tk.Label(self, text='Label B', bg='orange')
        label_c = tk.Label(self, text='Label C', bg='red')
        label_d = tk.Label(self, text='Label D', bg='green')
        label_e = tk.Label(self, text='Label E', bg='blue')
        opts = {'ipadx':10, 'ipady':10, 'fill':tk.BOTH}
        label_a.pack(side=tk.TOP, **opts)
        label_b.pack(side=tk.TOP, **opts)
        label_c.pack(side=tk.LEFT, **opts)
        label_d.pack(side=tk.LEFT, **opts)
        label_e.pack(side=tk.LEFT, **opts)
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var = tk.StringVar()
        self.var.trace("w", self.show_message)
        self.entry = tk.Entry(self, textvariable=self.var)
        self.btn = tk.Button(self, text="Clear", command=lambda: self.var.set(""))

        self.label = tk.Label(self)
        self.entry.pack()
        self.btn.pack()
        self.label.pack()
    def show_message(self, *args):  #recibe tres argumentos:
                                    #1: el nombre de la variable interna
                                    #2: una cadena vacía (se usa en otros tipos de Tk variables)
                                    #3: el modo que activó la operación ('w', 'r' o 'u')
        value = self.var.get()
        text = "Hello, {}!".format(value) if value else ""
        self.label.config(text=text)
if __name__ == "__main__":
    app = App()
    app.mainloop()
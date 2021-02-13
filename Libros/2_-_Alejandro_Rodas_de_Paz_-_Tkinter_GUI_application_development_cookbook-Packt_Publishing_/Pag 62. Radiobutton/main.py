import tkinter as tk


COLORS = [("Red", "red"), ("Green", "green"), ("Blue", "blue"), ("Black", "black")]
class ChoiceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var = tk.StringVar()
        self.var.set("red")
        self.buttons = [self.create_radio(c) for c in COLORS]
        for button in self.buttons:
            button.pack(anchor=tk.W, padx=10, pady=5)
    #Para evitar repetir el código de la inicialización de Radiobutton, nosotros
    #definió un método de utilidad que se llama desde una comprensión de lista.
    #Descomprimimos los valores de cada tupla de la lista COLORES y luego
    #pasó estas variables locales como opciones a Radiobutton. Recuerda
    #intenta no repetirte siempre que sea posible.
    #Como StringVar se comparte entre todas las instancias de Radiobutton, son
    #conectado automáticamente, y obligamos al usuario a seleccionar solo uno
    #elección.
    def create_radio(self, option):
        text, value = option
        return tk.Radiobutton(self, text=text, value=value, command=self.print_option, variable=self.var)

    def print_option(self):
        print(self.var.get())
if __name__ == "__main__":
    app = ChoiceApp()
    app.mainloop()
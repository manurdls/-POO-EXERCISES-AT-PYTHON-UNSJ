import re
import tkinter as tk

#En caso de que no esté familiarizado con el módulo re, puede consultar
#la introducción detallada a las expresiones regulares en el oficial
#Documentación de Python en https://docs.python.org/3.6/howto/regex.html.

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.pattern = re.compile("^\w{0,10}$")
        self.label = tk.Label(self, text="Enter your username")
        vcmd = (self.register(self.validate_username), "%i", "%P")  # En general, puede usar cualquiera de las siguientes
                                                                    # sustituciones:
                                                                    # % d: tipo de acción; 1 para inserción, 0 para
                                                                    #      eliminación y -1 de otra manera
                                                                    # % i: índice de la cadena que se inserta o elimina
                                                                    # % P: valor de la entrada si se permite la modificación
                                                                    # % s: valor de la entrada antes de la modificación
                                                                    # % S: contenido de cadena que se inserta o elimina
                                                                    # % v: el tipo de validación establecido actualmente
                                                                    # % V: tipo de validación que activó la acción
                                                                    # % W: el nombre del widget de entrada

        self.entry = tk.Entry(self, validate="key",             # Con la opción de validate establecida en "key",
                                                                # activaremos la entrada validación que se activa en
                                                                # cualquier modificación de contenido. El valor por
                                                                # defecto de validate es "none", lo que significa
                                                                # que no hay validación.
                                                                # Otros valores posibles son "focusin" y "focusout",
                                                                # que validan cuando el widget obtiene o pierde el foco,
                                                                # respectivamente, o simplemente "focus" para validar en
                                                                # ambos casos. Alternativamente, podemos usar el valor
                                                                # "all" para validar en todas las situaciones.

                              validatecommand=vcmd,             # validatecommand se llama cada vez que validate es
                                                                # activada, y debería devolver verdadero si el nuevo
                                                                # contenido es válido, y falso de lo contrario.
                                                                # Ya que necesitamos más información para determinar
                                                                # si el contenido
                                                                # es válido o no, creamos un contenedor Tcl alrededor
                                                                # de nuestra función Python utilizando el método de
                                                                # registro de la clase Widget (self.register). Luego,
                                                                # puede agregar el porcentaje de sustitución para cada
                                                                # parámetro que se pasará a la Función de Python.
                                                                # Finalmente, agruparemos estos valores como Python tupla

                              invalidcommand=self.print_error)  # La opción de invalidcommand toma una función que se
                                                                # invoca cuando validatecommand devuelve False.
                                                                # El mismo porcentaje de sustituciones puede ser
                                                                # aplicado a esta opción, pero en nuestro ejemplo,
                                                                # pasamos directamente el Método print_error() de nuestra clase.

        self.label.pack()
        self.entry.pack(anchor=tk.W, padx=10, pady=10)
    def validate_username(self, index, username):
        print("Modification at index " + index)
        return self.pattern.match(username) is not None
    def print_error(self):
        print("Invalid username character")
if __name__ == "__main__":
    app = App()
    app.mainloop()
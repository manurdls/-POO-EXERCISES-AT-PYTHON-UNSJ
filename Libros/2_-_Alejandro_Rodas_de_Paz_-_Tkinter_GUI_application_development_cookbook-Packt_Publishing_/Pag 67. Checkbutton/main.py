import tkinter as tk


class SwitchApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var = tk.IntVar()
        self.cb = tk.Checkbutton(self, text="Active?", variable=self.var, command=self.print_value)

        self.cb.pack()
    def print_value(self):
        print(self.var.get())
if __name__ == "__main__":
    app = SwitchApp()
    app.mainloop()

# este es otro ejemplo de como usar Checkbutton:
#var = tk.StringVar()
#var.set("OFF")
#checkbutton_active = tk.Checkbutton(master, text="Active?", variable=self.var, onvalue="ON", offvalue="OFF", command=update_value)
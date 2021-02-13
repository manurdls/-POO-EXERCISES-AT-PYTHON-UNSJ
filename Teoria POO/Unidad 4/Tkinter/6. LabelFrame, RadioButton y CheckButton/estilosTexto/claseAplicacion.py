from tkinter import ttk, font
import tkinter as tk

class LabelConEstilo(tk.Tk):
    __texto = None
    def __init__(self):
        super().__init__()
        self.title('Ejemplo')
        self.resizable(0,0)
        self.geometry('380x250+600+200')
        self.config(padx=5, pady=5)

        fuente = font.Font(font='Verdana 10', weight='normal')

        #variable que controla mayuscula y minuscula del texto
        self.valorMM = tk.StringVar()

        #declaración y seteo de la variable que contendrá el texto
        self.__texto = tk.StringVar()
        self.__texto.set('Texto ejemplo')

        #variable que controla el color del texto
        self.color = tk.StringVar()

        #variables booleanas que controlan el estilo del texto
        self.subrayado = tk.BooleanVar()
        self.negrita = tk.BooleanVar()
        self.cursiva = tk.BooleanVar()
        self.tachado = tk.BooleanVar()

        #elementos de la ventana#
        self.textoLbl = ttk.Label(self, textvariable=self.__texto, font=fuente)
        opts = {'ipadx':15, 'ipady':15, 'sticky':'nswe'}
        self.textoLbl.grid(row=0, column=0, **opts, columnspan=2)
        tk.LabelFrame()
        labelFrameSeleccione = tk.LabelFrame(self,
                                             text='Seleccione',
                                             font=fuente,
                                             borderwidth=2,
                                             relief='raised',
                                             padx=5, pady=5)
        labelFrameSeleccione.grid(row=1, column=0, **opts)

        labelFrameMarque = tk.LabelFrame(self,
                                         text='Marque',
                                         borderwidth=2,
                                         relief='raised')
        labelFrameMarque.grid(row=1, column=1, **opts)

        labelFrameColor = tk.LabelFrame(self,
                                        text='Color',
                                        font=fuente,
                                        borderwidth=2,
                                        relief='raised',
                                        padx=5, pady=5)
        labelFrameColor.grid(row=1, column=2, **opts)

        boton = ttk.Button(self, text='Reset', command=self.valoresPorDefecto)
        boton.grid(row=2, column=1,pady=15)
        #elementos de la ventana#

        #elementos del labelFrameSeleccione#
        ttk.Radiobutton(labelFrameSeleccione,
                        text='Mayúsculas',
                        value='mayusculas',
                        variable=self.valorMM,
                        command=self.cambiarValorMM).grid(row=0, column=0, columnspan=1, sticky='w')
        ttk.Radiobutton(labelFrameSeleccione,
                        text='Minúsculas',
                        value='minusculas',
                        variable=self.valorMM,
                        command=self.cambiarValorMM).grid(row=1, column=0, columnspan=1, sticky='w')
        #elementos del labelFrameSeleccione#

        #elementos del labelFrameMarque#
        ttk.Checkbutton(labelFrameMarque,
                        text='Subrayado',
                        variable=self.subrayado,
                        command=self.cambiarEstilo).grid(row=0, column=0, columnspan=1, sticky='w')
        ttk.Checkbutton(labelFrameMarque,
                        text='Negrita',
                        variable=self.negrita,
                        command=self.cambiarEstilo).grid(row=1, column=0, columnspan=1, sticky='w')
        ttk.Checkbutton(labelFrameMarque,
                        text='Cursiva',
                        variable=self.cursiva,
                        command=self.cambiarEstilo).grid(row=2, column=0, columnspan=1, sticky='w')
        ttk.Checkbutton(labelFrameMarque,
                        text='Tachado',
                        variable=self.tachado,
                        command=self.cambiarEstilo).grid(row=3, column=0, columnspan=1, sticky='w')
        #elementos del labelFrameMarque#

        #elementos del labelFrameColor#
        ttk.Radiobutton(labelFrameColor,
                        text='Negro',
                        value='negro',
                        variable=self.color,
                        command=self.cambiarColor).grid(row=0, column=0, columnspan=1, sticky='w')
        ttk.Radiobutton(labelFrameColor,
                        text='Rojo',
                        value='rojo',
                        variable=self.color,
                        command=self.cambiarColor).grid(row=1, column=0, columnspan=1, sticky='w')
        ttk.Radiobutton(labelFrameColor,
                        text='Azul',
                        value='azul',
                        variable=self.color,
                        command=self.cambiarColor).grid(row=2, column=0, columnspan=1, sticky='w')
        #elementos del labelFrameColor#

        self.valoresPorDefecto()
        self.mainloop()

    def cambiarValorMM(self):
        if self.valorMM.get() == 'minusculas':
            self.__texto.set(self.__texto.get().lower())
        else:
            self.__texto.set(self.__texto.get().upper())

    def cambiarEstilo(self):
        subrayado=' underline ' if self.subrayado.get()==True else''    ##
        negrita=' bold ' if self.negrita.get()==True else ''            ##
        cursiva=' italic ' if self.cursiva.get()==True else ''          ##      IMPORTANTE
        tachado=' overstrike ' if self.tachado.get()==True else ''      ##      IMPORTANTE
        fuente='Verdana 10'+subrayado+negrita+cursiva+tachado           ##
        self.textoLbl.configure(font=fuente)                            ##

    def cambiarColor(self):
        if self.color.get() == 'negro':
            self.textoLbl.config(foreground='black')
        else:
            if self.color.get() == 'rojo':
                self.textoLbl.config(foreground='red')
            else:
                if self.color.get() == 'azul':
                    self.textoLbl.config(foreground='blue')

    def valoresPorDefecto(self):
        self.valorMM.set('minusculas')
        self.cambiarValorMM()
        self.subrayado.set(False)
        self.cursiva.set(False)
        self.negrita.set(False)
        self.tachado.set(False)
        self.cambiarEstilo()
        self.color.set('negro')
        self.cambiarColor()

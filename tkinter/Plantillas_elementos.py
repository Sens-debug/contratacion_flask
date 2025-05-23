import tkinter as tk
from tkinter import filedialog, messagebox

class Plantilla_etiqueta(tk.Label):
    def __init__(self, master,text):
        super().__init__(master,text=text)

class Plantilla_entrada_datos(tk.Entry):
    def __init__(self, master,variable_texto):
        super().__init__(master, textvariable=variable_texto)

class Plantilla_boton(tk.Button):
    def __init__(self, master,funcion, titulo):
        super().__init__(master, command= funcion, text=titulo)

class Plantilla_ventana_secundaria(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)

class Plantilla_marco(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
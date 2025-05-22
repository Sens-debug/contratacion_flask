# client_gui.py
import tkinter as tk
from tkinter import filedialog, messagebox
import requests

class Plantilla_etiqueta(tk.Label):
    def __init__(self, master,text):
        super().__init__(master,text=text)

class Plantilla_entrada_datos(tk.Entry):
    def __init__(self, master,variable_texto):
        super().__init__(master, textvariable=variable_texto)

class Plantilla_boton(tk.Button):
    def __init__(self, master,funcion, titulo):
        super().__init__(master, command= funcion, text=titulo)


class Pagina_inicio_sesion(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.configure(bg="lightgray")
        self.title("Inicio Sesion")
        self.resizable(0,0)
        self.geometry('200x250')
        marco_inicio_sesion=tk.Frame().pack()
        Plantilla_etiqueta(marco_inicio_sesion,"CONTRATACION IPSTID").pack(pady=20)
        Plantilla_etiqueta(marco_inicio_sesion,"Bienvenido Al inicio de Sesion").pack(pady=10)
        Plantilla_etiqueta(marco_inicio_sesion,"Usuario").pack(pady=2)
        variable_usuario= tk.StringVar()
        Plantilla_entrada_datos(marco_inicio_sesion,variable_usuario).pack()
        Plantilla_etiqueta(marco_inicio_sesion,"Contraseña").pack(pady=2)
        variable_contraseña = tk.StringVar()
        Plantilla_entrada_datos(marco_inicio_sesion, variable_texto=variable_contraseña).pack()
        Plantilla_boton(marco_inicio_sesion,lambda :self.enviar_credenciales_inicio_sesion(variable_usuario.get(), variable_contraseña.get()),"INICIO SESION").pack()
        self.estado = Plantilla_etiqueta(marco_inicio_sesion,"")
        self.estado.pack()
        self.mainloop()
    
    def enviar_credenciales_inicio_sesion(self,usuario, contraseña):
        
        peticion_https = {"usuario":usuario,
                         "contrasena":contraseña
                         }
        try:
            res = requests.post("http://127.0.0.1:5000/inicio_sesion",json=peticion_https)
            respuesta = res.json()
            

            if respuesta["estado"] == "aprobado":
                if respuesta["id"] == 1:
                    #Entramos en la GUI ADMIN
                    self.estado.config(text="INICIO ADMIN")
                    return
                #Entramos en la GUI Normal
                self.estado.config(text="Inicio Usuario")
            if respuesta["estado"] == "denegado":
                self.estado.config(text="ACCESO DENEGADO")
        finally:
            pass
        

Pagina_inicio_sesion()

# def upload_file():
#     '''Funcion encargada de abrir el selector de archivo y
#       enviar lo seleccionado al servidor de flask alojado en la URI delarada internamente'''

#     #Almacena el path del archivo seleciionado a través de la interfaz
#     file_path = filedialog.askopenfilename()
#     #Si no selecciona ningun archivo ->Path vacio -> Accede al early return
#     if not file_path:
#         return
#     try:
#         with open(file_path, 'rb') as f:
#             files = {'file': f}
#             response = requests.post('http://127.0.0.1:5000/subir', files=files)
#         #Levantya un message box que contiene el mensaje de respuesta de la peticion a la URI
#         messagebox.showinfo("Respuesta", response.text)
#     except Exception as e:
#         messagebox.showerror("Error", str(e))

# root = tk.Tk()
# root.title("Subir archivo al servidor Flask")

# btn_upload = tk.Button(root, text="Seleccionar y Subir Archivo", command=upload_file)
# btn_upload.pack(padx=20, pady=20)

# root.mainloop()

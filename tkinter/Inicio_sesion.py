# client_gui.py
import tkinter as tk
from Plantillas_elementos import *
import requests
from Interfaz_usuario import *
import time


class Pagina_inicio_sesion(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.configure(bg="lightgray")
        self.title("Inicio Sesion")
        self.attributes('-topmost', True)
        self.resizable(1,1)
        self.geometry('200x250')
        marco_inicio_sesion=Plantilla_marco()
        marco_inicio_sesion.grid(row=0,column=0)
        Plantilla_etiqueta(marco_inicio_sesion,"CONTRATACION IPSTID").grid(row=0,pady=20)
        Plantilla_etiqueta(marco_inicio_sesion,"Bienvenido Al inicio de Sesion").grid(row=1,pady=10)
        Plantilla_etiqueta(marco_inicio_sesion,"Usuario").grid(row=2,pady=2)
        variable_usuario= tk.StringVar()
        Plantilla_entrada_datos(marco_inicio_sesion,variable_usuario).grid(row=3)
        Plantilla_etiqueta(marco_inicio_sesion,"Contraseña").grid(row=4,pady=2)
        variable_contraseña = tk.StringVar()
        Plantilla_entrada_datos(marco_inicio_sesion, variable_texto=variable_contraseña).grid(row=5)
        Plantilla_boton(marco_inicio_sesion,lambda :self.enviar_credenciales_inicio_sesion(variable_usuario.get(), variable_contraseña.get()),"INICIO SESION").grid(row=6)
        self.estado = Plantilla_etiqueta(marco_inicio_sesion,"")
        self.estado.grid(row=7)
        
    def enviar_credenciales_inicio_sesion(self,usuario, contraseña):
        
        peticion_https = {"usuario":usuario,
                         "contrasena":contraseña
                         }
        try:
            res = requests.post("http://127.0.0.1:5000/inicio_sesion",json=peticion_https)
            respuesta = res.json()
            

            if respuesta["estado"] == "aprobado":
                nombre_usuario = respuesta["nombre_usuario"]
                #Entramos en la GUI
                self.estado.config(text="Inicio Usuario")
                time.sleep(0.5)
                self.interfaz_usuario= None
                self.crear_ventana_interfaz(nombre_usuario,respuesta)
                
            if respuesta["estado"] == "denegado":
                self.estado.config(text="ACCESO DENEGADO")


        except Exception as e:
            messagebox.showerror("ERROR", e)
            print(e)
    def crear_ventana_interfaz(self,nombre_usuario,json_datos_usuario):
        if not self.interfaz_usuario or not self.interfaz_usuario.winfo_exist():
            self.interfaz_usuario =  Interfaz_usuario(nombre_usuario,self,json_datos_usuario)
        else:
            self.interfaz_usuario.lift()
            





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

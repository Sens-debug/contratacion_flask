import tkinter as tk
import requests
from Plantillas_elementos import *

class Interfaz_usuario (Plantilla_ventana_secundaria):
    def __init__(self, nombre_usuario, padre, json_usuario ):
        super().__init__(master=padre)
        padre.withdraw()
        self.title("Interfaz Usuario")
        
        cuadro_rutas =tk.Frame(self, relief= 'raised',bd=2)
        cuadro_rutas.grid(row=0,column=0)
        
        try:
            peticion = requests.post("http://127.0.0.1:5000/obtener_cantidad_archivos", json= json_usuario)
            respuesta = peticion.json()
            fila_Label=0
            fila_boton=1
            print(respuesta["respuesta"])
            for i in (respuesta["respuesta"]):
                
                Plantilla_etiqueta(self, f"{i[0]}").grid(row=fila_Label,column=0)
                Plantilla_boton(self,lambda:self.solicitar_eleccion_archivo(),"x").grid(row=fila_boton,column=0)
                fila_Label+=2
                fila_boton+=2
                
        except Exception as e:
            print(e)
        
        

        

        self.protocol("WM_DELETE_WINDOW", lambda :self.al_cerrar(padre))

    
    
    
    def al_cerrar(self,padre):
        padre.deiconify()
        self.destroy()

    def solicitar_eleccion_archivo(self):
        filedialog.askopenfile(mode='rb', filetypes=[("Archivos PDF", "*.pdf")])

# client_gui.py
import tkinter as tk
from tkinter import filedialog, messagebox
import requests

def upload_file():
    '''Funcion encargada de abrir el selector de archivo y enviar lo seleccionado al servidor de flask alojado en la URI delarada internamente'''

    #Almacena el path del archivo seleciionado a través de la interfaz
    file_path = filedialog.askopenfilename()
    #Si no selecciona ningun archivo ->Path vacio -> Accede al early return
    if not file_path:
        return
    try:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post('http://127.0.0.1:5000/subir', files=files)
        #Levantya un message box que contiene el mensaje de respuesta de la peticion a la URI
        messagebox.showinfo("Respuesta", response.text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Subir archivo al servidor Flask")

btn_upload = tk.Button(root, text="Seleccionar y Subir Archivo", command=upload_file)
btn_upload.pack(padx=20, pady=20)

root.mainloop()

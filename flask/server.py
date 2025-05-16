from flask import Flask, request
import os


app = Flask(__name__)
carpeta_subida = 'nuevos'
#Crea una carpeta nueva, si existe la selecciona, si no existe la crea ->No levanta excepcion si ya existe
os.makedirs(carpeta_subida, exist_ok=True)
#Establece la ruta en la que se va a ejecitar esta funcion y el metodo que manejará
@app.route('/subir', methods = ['POST'])
def subir_archivo():
    '''Funcion encargada de subir los archivos al servidor de archivos
    No recibe parametros, metodo Post'''

    #si la peticion no contiene ningun archuvo entonces accede al early return(STATUS_CODE=400)
    if 'file' not in request.files:
        return 'No hay archivo en la peticion', 400
    
    archivo = request.files['file']
    #Si el archivo no tiene nombre accede al early return (STATUS_CODE=400)
    if archivo.filename == '':
        return 'No selected file', 400
    
    #Crea la ruta de archivo en una variable, compuesta por (PATH_PROYECTO+CARPETA_SUBIDA+NOMBRE_ARCHIVO)
    ruta_del_archivo = os.path.join(carpeta_subida, archivo.filename)
    #Guarda el archivo en la ruta
    archivo.save(ruta_del_archivo)
    #Si llega hasta este punto entonces accede al return que entrega el mensaje de "Archivo subido satisfactoriamente (STATUS_CODE=200)"
    return f'Archivo {archivo.filename} se ha subido satisfactoriamente', 200

if __name__ == '__main__':  
    app.run(debug=True, port=5000)
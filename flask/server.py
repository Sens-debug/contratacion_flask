from flask import Flask, request, jsonify
import mysql.connector
import os

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="prueba_contratacion"
)

app = Flask(__name__)

@app.route('/inicio_sesion',methods=['POST'])
def verificar_inicio_sesion():
    try:
        datos = request.json
        usuario= datos.get("usuario")
        contraseña= datos.get("contrasena")
        cursor = conexion.cursor()
        cursor.execute(f"select * from usuarios where nombre_usuario=%s and contraseña_usuario=%s",(usuario,contraseña))
        res=cursor.fetchone()
        
        if res:
            id= res[0]
            return jsonify({"estado":"aprobado",
                            f"id":id}),200
        else:
            return jsonify({"estado":"denegado"}),200
    finally:
        pass
# @app.route('/subir', methods = ['POST'])
# def subir_archivo():
#     '''Funcion encargada de subir los archivos al servidor de archivos
#     No recibe parametros, metodo Post'''


#     carpeta_subida = 'nuevos'
#     #Crea una carpeta nueva, si existe la selecciona, si no existe la crea ->No levanta excepcion si ya existe
#     os.makedirs(carpeta_subida, exist_ok=True)
#     #Establece la ruta en la que se va a ejecitar esta funcion y el metodo que manejará

#     #si la peticion no contiene ningun archuvo entonces accede al early return(STATUS_CODE=400)
#     if 'file' not in request.files:
#         return 'No hay archivo en la peticion', 400
    
#     archivo = request.files['file']
#     #Si el archivo no tiene nombre accede al early return (STATUS_CODE=400)
#     if archivo.filename == '':
#         return 'No selected file', 400
    
#     #Crea la ruta de archivo en una variable, compuesta por (PATH_PROYECTO+CARPETA_SUBIDA+NOMBRE_ARCHIVO)
#     ruta_del_archivo = os.path.join(carpeta_subida, archivo.filename)
#     #Guarda el archivo en la ruta
#     archivo.save(ruta_del_archivo)
#     #Si llega hasta este punto entonces accede al return que entrega el mensaje de "Archivo subido satisfactoriamente (STATUS_CODE=200)"
#     return f'Archivo {archivo.filename} se ha subido satisfactoriamente', 200

if __name__ == '__main__':  
    app.run(debug=True,  host= '0.0.0.0' ,port=5000)
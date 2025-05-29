from flask import Flask, request, jsonify
import mysql.connector
import os
import numpy as np
from flask_cors import CORS
import magic
import fitz  # Para PDF
from PIL import Image
import io

import firma_fomatos.firma_documentos

def obtener_conexion_bd():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="try_contratacion"
    )
    
app = Flask(__name__)
#Los cors nos permiten trabajar con react
CORS(app)
@app.route('/inicio_sesion',methods=['POST'])
def verificar_inicio_sesion():
    try:
        conexion = obtener_conexion_bd()
        datos = request.json
        usuario= datos.get("usuario")
        contraseña= datos.get("contraseña")
        cursor = conexion.cursor(buffered=True)
        cursor.execute(f"""select usuarios.primer_nombre, usuarios.primer_apellido, usuarios.correo,cargos.Cargo, cargos.id, usuarios.id 
                       from usuarios 
                       INNER JOIN cargos on cargos.id = usuarios.cargo_id 
                       INNER JOIN documentosxcargoxestado on documentosxcargoxestado.cargo_id=cargos.id 
                       INNER JOIN documentos on documentos.id=documentosxcargoxestado.documento_id 
                       where nombre_usuario=%s and contraseña_usuario=%s""",(usuario,contraseña,))
        res=cursor.fetchone()
        cursor.close()
        conexion.close()
        if res:
            primer_nombre=res[0]
            primer_apellido=res[1]
            correo=res[2]
            cargo=res[3]
            id_cargo=res[4]
            id_usuario = res [5]
            return jsonify({"estado":"aprobado",
                            "primer_nombre":primer_nombre,
                            "primer_apellido":primer_apellido,
                            "correo":correo,
                            "cargo":cargo,
                            "id_cargo":id_cargo,
                            "id_usuario":id_usuario
                            }
                            ),200
        else:
            return jsonify({"estado":"denegado"}),200
    finally:
        pass
@app.route('/obtener_cantidad_archivos',methods=['POST'])
def obtener_cantidad_archivos_a_subir():
    conexion = obtener_conexion_bd()
    datos = request.json
    id_usuario = datos.get("id_usuario")
    print(datos)
    cursor = conexion.cursor(buffered=True)
    cursor.execute("""SELECT 
    d.documento AS documento_requerido
    FROM usuarios u
    -- Relación con cargo
    INNER JOIN cargos c ON u.cargo_id = c.id
    -- Relación con el estado actual del usuario
    INNER JOIN usuariosxestado ue ON u.id = ue.id_usuario
    INNER JOIN estados e ON ue.estado_id = e.id
    -- Relación con documentos requeridos por cargo y estado
    INNER JOIN documentosxcargoxestado dce 
        ON dce.cargo_id = u.cargo_id AND dce.estado_id = ue.estado_id
    -- Relación con los nombres de documentos
    INNER JOIN documentos d ON d.id = dce.documento_id
 = %s; """,(id_usuario,))
    respuesta =cursor.fetchall()
    print(respuesta)
    cursor.close()
    conexion.close()
    if respuesta:
        
        cantidad_elementos= len(respuesta)
        elementos_array =np.array(respuesta)
        return jsonify({"respuesta":respuesta,
                        "cantidad_elementos":cantidad_elementos}),200
    else: 
        return jsonify({"respuesta":"imposible continuar"},400)

@app.route('/obtener_usuarios', methods=['GET'])
def obtener_usuarios():
    conexion = obtener_conexion_bd()
    cursor = conexion.cursor(buffered=True)
    cursor.execute("select nombre_usuario from usuarios")
    respuesta = cursor.fetchall()
    print(respuesta)
    cursor.close()
    conexion.close()
    return jsonify({"respuesta":respuesta})

@app.route('/upload', methods=['POST'])
def upload_file():
    id_usuario = request.form.get('id_usuario')
    cargo = request.form.get("cargo")
    print(f"id buscado {id_usuario}")

    conexion = obtener_conexion_bd()
    cursor = conexion.cursor()
    cursor.execute(f"""select 
                  upper(CONCAT_WS(' ', primer_nombre, segundo_nombre, primer_apellido, segundo_apellido))
                   from usuarios where id =%s 
                    """,(id_usuario,))
    nombre_completo = cursor.fetchone()[0]
    print(nombre_completo)
    cursor.close()
    conexion.close()

    if not request.files:
        return jsonify({"mensaje": "No se enviaron archivos."}), 400
    archivos = request.files
    firmas_validas = ['image/jpeg', 'image/png', 'application/pdf']
    errores = []
    print(archivos)
    mime = magic.Magic(mime=True)  # Usa instancia segura

    for nombre_archivo, archivo in archivos.items():
        contenido = archivo.read()

        # if not contenido:
        #     errores.append(f"{nombre_archivo}: archivo vacío.")
        #     continue

        tipo_mime = mime.from_buffer(contenido)
        print(f"{nombre_archivo} tipo: {tipo_mime}")
       

        if tipo_mime not in firmas_validas:
            errores.append(f"{nombre_archivo}: tipo no permitido ({tipo_mime})")
            continue

        # Verificacion profunda de los pdf
        if tipo_mime == 'application/pdf':
            try:
                with fitz.open(stream=contenido, filetype="pdf") as doc:
                    if doc.page_count == 0:
                        raise ValueError("El PDF no tiene páginas.")
            except Exception as e:
                errores.append(f"{nombre_archivo}: PDF no válido ({e})")
                continue
                
        # Verificacion profunda imagen
        elif tipo_mime in ['image/jpeg', 'image/png']:
            try:
                image = Image.open(io.BytesIO(contenido))
                image.verify()  # Verifica que la imagen no está corrupta
                # Opcional: cargar realmente para validar más
                image = Image.open(io.BytesIO(contenido))
                image.load()
                # Opcional: validar tamaño mínimo, por ejemplo
            except Exception as e:
                errores.append(f"{nombre_archivo}: imagen no válida ({e})")
                continue

        

        
        # os.makedirs(f"archivos/{nombre_usuario}", exist_ok=True)
        # print("aa")
        ruta_carpeta_script = os.path.dirname(__file__)
        ruta_carpeta_archivos = os.path.join(ruta_carpeta_script,"archivos")
        
        os.makedirs(fr"{ruta_carpeta_archivos}\{nombre_completo}", exist_ok=True)
        ruta_carpeta_persona  = os.path.join(ruta_carpeta_archivos,nombre_completo)
        
        try:
            with open(fr"{ruta_carpeta_persona}\{nombre_archivo}_{nombre_completo}.pdf" ,"wb") as f:
                f.write(contenido)
                print(" es escribio")
        except Exception as e:
            errores.append({"no cargó el archivo":e})

        from firma_fomatos.firma_documentos import Firma_documentos
        firma =Firma_documentos('','','DSFD','DFS',nombre_completo,'','96851577','ipstid@ipstid.com','255524','pp','','0+',ruta_carpeta_persona)
        
        firma.firmar_formatos_administrativo()
        # Firma de los formatos posterior a subir la firma

    if errores:
        return jsonify({
            "mensaje": f"Algunos archivos no se subieron.{errores}"
        }), 400

    return jsonify({"mensaje": "Archivos subidos correctamente."}), 200

@app.route('/campos_creacion_usuario', methods =['GET'])
def obtener_campos_crear_usuarios():
    conexion =obtener_conexion_bd()
    cursor = conexion.cursor(buffered=True)
    cursor.execute("""SELECT COLUMN_NAME 
                   FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE TABLE_NAME = 'usuarios'
                    and TABLE_SCHEMA = 'try_contratacion'""")
    columnas_base_datos = cursor.fetchall()
    retorno = {}
    for columna in columnas_base_datos:
        retorno[str(columna[0])]=columna[0]
    return jsonify({'retorno':retorno})

if __name__ == '__main__':  
    app.run(debug=True,  host= '0.0.0.0' ,port=5000)
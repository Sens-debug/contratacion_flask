from flask import Flask, request, jsonify
import mysql.connector
import os
import numpy as np
from flask_cors import CORS
import magic
import fitz  # Para PDF
from PIL import Image
import io

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
        cursor.execute(f"""select 
                        upper(CONCAT_WS('_',usuarios.primer_nombre,usuarios.segundo_nombre,usuarios.primer_apellido,usuarios.segundo_apellido)) as nombre_completo,
                        usuarios.direccion_residencia as direccion,
                        usuarios.cedula_ciudadania as cedula,
                        usuarios.correo_electronico as correo,
                        cargos.Cargo as cargo,
                        cargos.id as Cargo_id,
                        areas.area as area,
                        tipos_sangre.tipo as RH,
                        usuarios.fecha_nacimiento as f_nacimiento,
                        usuarios.telefono as Tel,
                        usuarios.id as ID_usuario
                        from usuarios 
                        INNER JOIN tipos_sangre on tipos_sangre.id = usuarios.tipo_sangre_id
                        INNER JOIN cargos on cargos.id = usuarios.cargo_id 
                        INNER JOIN cargosxarea on cargos.id = cargosxarea.cargo_id
                        INNER JOIN areas on areas.id= cargosxarea.area_id
                       where usuarios.nombre_usuario = %s and usuarios.contraseña_usuario=%s""",(usuario,contraseña,))
        res=cursor.fetchone()
        
        if res:
            nombre_completo=res[0]
            direccion=res[1]
            cedula=res[2]
            correo=res[3]
            cargo=res[4]
            cargo_id = res [5]
            area = res [6]
            rh = res [7]
            f_nacimiento = res [8]
            tel = res [9]
            id_usuario = res [10]
            return jsonify({"estado":"aprobado",
                            "nombre_completo":nombre_completo,
                            "direccion":direccion,
                            "cedula":cedula,
                            "correo":correo,
                            "cargo":cargo,
                            "cargo_id":cargo_id,
                            "area":area,
                            "rh":rh,
                            "f_nacimiento":f_nacimiento,
                            "tel":tel,
                            "id_usuario":id_usuario
                            }
                            ),200
        else:
            return jsonify({"estado":"denegado"}),200
    finally:
        cursor.close()
        conexion.close()


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
    # print(respuesta)
    cursor.close()
    conexion.close()
    if respuesta:
        
        cantidad_elementos= len(respuesta)
        print(cantidad_elementos)
        elementos_array =np.array(respuesta)
        return jsonify({"respuesta":respuesta,
                        "cantidad_elementos":cantidad_elementos}),200
    else: 
        return jsonify({"respuesta":"imposible continuar"},400)


def comprobar_tipo_archivos (nombre_archivo,contenido_archivo, errores):
    mime = magic.Magic(mime=True)  # Usa instancia segura
    firmas_validas = ['image/jpeg', 'image/png', 'application/pdf']

    tipo_mime = mime.from_buffer(contenido_archivo)
    print(f"{nombre_archivo} tipo: {tipo_mime}")
    
    if tipo_mime not in firmas_validas:
        errores.append(f"{nombre_archivo}: tipo no permitido ({tipo_mime})")
        return
    # Verificacion profunda de los pdf
    if tipo_mime == 'application/pdf':
        try:
            with fitz.open(stream=contenido_archivo, filetype="pdf") as doc:
                if doc.page_count == 0:
                    raise ValueError("El PDF no tiene páginas.")
        except Exception as e:
            errores.append(f"{nombre_archivo}: PDF no válido ({e})")
            return
            
    # Verificacion profunda imagen
    elif tipo_mime in ['image/jpeg', 'image/png']:
        try:
            image = Image.open(io.BytesIO(contenido_archivo))
            image.verify()  # Verifica que la imagen no está corrupta
            # Opcional: cargar realmente para validar más
            image = Image.open(io.BytesIO(contenido_archivo))
            image.load()
    
    
            # Opcional: validar tamaño mínimo, por ejemplo
        except Exception as e:
            errores.append(f"{nombre_archivo}: imagen no válida ({e})")
            return
        
    return tipo_mime

@app.route('/upload', methods=['POST'])
def upload_file():
    nombre_completo = request.form.get('nombre_completo')
    id_usuario = request.form.get('id_usuario')
    direccion = request.form.get('direccion')
    cedula = request.form.get('cedula')
    correo_electronico = request.form.get('correo')
    cargo = request.form.get("cargo")
    area = request.form.get('area')
    tipo_sangre = request.form.get('rh')
    fecha_nacimiento = request.form.get('f_nacimiento')
    telefono = request.form.get('tel')
    cargo_id = request.form.get('cargo_id')
    
    # print(f"id buscado {id_usuario}")


    # if not request.files:
    #     return jsonify({"mensaje": "No se enviaron archivos."}), 400
    archivos = request.files
    
    errores = []
    print(archivos)
    

    for nombre_archivo, archivo in archivos.items():
        contenido = archivo.read()
        print(nombre_archivo)

        # if not contenido:
        #     errores.append(f"{nombre_archivo}: archivo vacío.")
        #     continue

        tipo_archivo =comprobar_tipo_archivos(nombre_archivo,contenido,errores)
        if tipo_archivo == 'image/jpeg' or tipo_archivo=='image/png':
            tipo_archivo= tipo_archivo[6:]
        if tipo_archivo == 'application/pdf':
            tipo_archivo = tipo_archivo[12:]
       
        
        ruta_carpeta_script = os.path.dirname(__file__)
        ruta_carpeta_archivos = os.path.join(ruta_carpeta_script,"archivos")
        
        os.makedirs(fr"{ruta_carpeta_archivos}\{area}\{cargo}\{nombre_completo}", exist_ok=True)
        ruta_carpeta_persona  = os.path.join(ruta_carpeta_archivos,area,cargo,nombre_completo)
        print(ruta_carpeta_persona)
        
        try:
            with open(fr"{ruta_carpeta_persona}\{nombre_archivo}_{nombre_completo}.{tipo_archivo}" ,"wb") as f:
                
                f.write(contenido)

        except Exception as e:
            errores.append({"no cargó el archivo":e})
        if nombre_archivo == 'Firma':
            conexion = obtener_conexion_bd().cursor()
            conexion.execute('update usuarios set ruta_firma =%s where usuarios.id ')
            pass
        

        from firma_fomatos.firma_documentos import Firma_documentos
        firma =Firma_documentos(nombre_completo,direccion,cedula,correo_electronico,telefono,area,cargo,tipo_sangre,fecha_nacimiento, ruta_carpeta_persona)
    if errores:
        if cargo_id =='1':
            firma.firmar_formatos_antibiotico()
        # elif cargo ==2

        return jsonify({
            "mensaje": f"Algunos archivos no se subieron.{errores}"
        }), 400
    if cargo_id =='1':
        firma.firmar_formatos_antibiotico()
    
    # Firma de los formatos posterior a subir la firma

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
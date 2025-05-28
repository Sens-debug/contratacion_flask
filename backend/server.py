from flask import Flask, request, jsonify
import mysql.connector
import os
import numpy as np
from flask_cors import CORS
import magic

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
    nombre_usuario = request.form.get('nombre_usuario')
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
        print(nombre_usuario)

        if tipo_mime not in firmas_validas:
            errores.append(f"{nombre_archivo}: tipo no permitido ({tipo_mime})")
            continue
        
        os.makedirs(f"archivos/{nombre_usuario}", exist_ok=True)
        print("aa")
        with open(f"archivos/{nombre_usuario}/{nombre_archivo}_{nombre_usuario}", "wb") as f:
            f.write(contenido)

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
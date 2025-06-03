from flask import Flask, request, jsonify
import mysql.connector
import os
import numpy as np
from flask_cors import CORS
import magic
import fitz  # Para PDF
from PIL import Image
import io
import datetime

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
        print(datos)
        usuario= datos.get("usuario")
        contraseña= datos.get("contraseña")
        cursor = conexion.cursor(buffered=True)
        cursor.execute("""select 
                        upper(CONCAT_WS(' ',usuarios.primer_nombre,usuarios.segundo_nombre,usuarios.primer_apellido,usuarios.segundo_apellido)) as nombre_completo,
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
        cursor.close()
        conexion.close()
        print(res)

        
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
            return jsonify({"estado":"denegado"}),400
    finally:
        pass

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    informacion =request.json
    print(informacion)
    primer_nombre = informacion.get("Primer_nombre")
    segundo_nombre = informacion.get("Segundo_nombre")
    primer_apellido = informacion.get("Primer_apellido")
    segundo_apellido = informacion.get("Segundo_apellido")
    direccion = informacion.get("Direccion_Residencia")
    cedula = informacion.get("Cedula_ciudadania")
    correo = informacion.get("Correo_electronico")
    telefono = informacion.get("Telefono")
    Nombre_usuario = informacion.get("Nombre_Usuario")
    Contraseña_usuario = informacion.get("Contraseña_usuario")
    cargo_seleccionado_id = informacion.get("cargo_seleccionado") 
    tipo_sangre_seleccionado_id = informacion.get("tipo_sangre_seleccionado") 
    dia_nacimiento = informacion.get("fecha_nacimiento")["day"]
    mes_nacimiento = informacion.get("fecha_nacimiento")["month"]
    año_nacimiento = informacion.get("fecha_nacimiento")["year"]
    fecha_nacimiento = datetime.date(año_nacimiento,mes_nacimiento,dia_nacimiento)
    print(Contraseña_usuario)

    

    try:
        conexion = obtener_conexion_bd()
        cursor = conexion.cursor()
        cursor.execute("""INSERT INTO usuarios
                       (id,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,
                        direccion_residencia,cedula_ciudadania,correo_electronico,
                        cargo_id,tipo_sangre_id,telefono,ruta_firma,nombre_usuario,contraseña_usuario,fecha_nacimiento,estado_firma) 
                        VALUES
                        (%s,%s,%s,%s,%s,
                            %s,%s,%s,
                            %s,%s,%s,%s,
                            %s,%s,%s,%s);""",(None,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,
                                         direccion,cedula,correo,
                                         cargo_seleccionado_id,tipo_sangre_seleccionado_id,telefono,None,
                                         Nombre_usuario,Contraseña_usuario,fecha_nacimiento,0 ))
        conexion.commit()
        cursor.execute("select id from usuarios where cedula_ciudadania =%s",(cedula,))
        id_usuario = cursor.fetchone()
        print(id_usuario[0])
        cursor.execute("""INSERT INTO usuariosxestado (id_usuario,estado_id) VALUES (%s,%s)""",(id_usuario[0],1))
        conexion.commit()
        cursor.close()
        conexion.close()
        return jsonify({"mensaje":"Creacion de usuario Exitosa"}),200
    except Exception as e:
        print(e)
        return jsonify ({"mensaje":f"Error en la creacion de usuario{e}"}),400

@app.route('/obtener_usuarios', methods= ['GET'])
def obtener_id_nombre_usuarios():
    try:
        print("holo")
        conexion = obtener_conexion_bd()
        cursor =conexion.cursor()
        cursor.execute("select id, primer_nombre, primer_apellido, cedula_ciudadania from usuarios")
        res=cursor.fetchall()
        print(res)
        return jsonify({"mensaje":"Fetch Exitoso"
                        ,"usuarios":res}),200
    except Exception as e:
        return jsonify({"mensaje":f"Error en el metodo{e}"}),400

@app.route('/obtener_estados_contratacion', methods=['GET'])
def obtener_estados_contratacion():
    try:
        conexion = obtener_conexion_bd()
        cursor = conexion.cursor()
        cursor.execute("select id, estado from estados")
        res = cursor.fetchall()
        return jsonify({"estados":res,
                        "mensaje":"fetch exitoso"}),200
    except Exception as e:
        return jsonify({"mensaje":f"Error en el fetch{e}"}),400

@app.route('/actualizar_estadoxusuario',methods=['POST'])
def actualizar_estadoxusuario():
    try:
        data = request.json
        id_usuario = data["id_usuario"]
        id_estado = data["id_estado"]
        conexion = obtener_conexion_bd()
        cursor = conexion.cursor()
        cursor.execute("""update usuariosxestado 
                       set usuariosxestado.estado_id=%s 
                       WHERE usuariosxestado.id_usuario=%s""", (id_estado,id_usuario))
        conexion.commit()
        cursor.close()
        conexion.close()
        return jsonify({"mensaje":"Datos_actualizados exitosamente"}),200
    except Exception as e:
        return jsonify({"mensaje":f"error en el post{e}"}),400

@app.route('/actualizar_estado_firma', methods=['POST'])
def actualizar_estado_firma():
    try:
        data = request.json
        id_estado_firma = data.get("estado_firma")
        id_usuario = data.get("id_usuario")
        conexion = obtener_conexion_bd()
        cursor = conexion.cursor()
        cursor.execute("""update usuarios
                        set usuarios.estado_firma=%s 
                       WHERE usuarios.id=%s""",(id_estado_firma,id_usuario))
        conexion.commit()
        cursor.close()
        conexion.close()
        return jsonify({"mensaje":"Actualizacion Exitosa"}),200
    except Exception as e: 
        return jsonify({"mensaje":f"Error en la actualizacion {e}"})

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
                   where u.id= %s; """,(id_usuario,))
    respuesta =cursor.fetchall()
    print(respuesta)
    cursor.close()
    conexion.close()
    if respuesta:
        
        cantidad_elementos= len(respuesta)
        print(cantidad_elementos)
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
    if not request.files:
        return jsonify({"mensaje": "No se enviaron archivos."}), 400
    archivos = request.files
    print(request.form)
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

    
    errores = []
    print(archivos)

    for nombre_archivo, archivo in archivos.items():
        contenido = archivo.read()
        print(nombre_archivo)

        tipo_archivo =comprobar_tipo_archivos(nombre_archivo,contenido,errores)
        if tipo_archivo == 'image/jpeg' or tipo_archivo=='image/png':
            tipo_archivo= tipo_archivo[6:]
        if tipo_archivo == 'application/pdf':
            tipo_archivo = tipo_archivo[12:]
       
        
        ruta_carpeta_script = os.path.dirname(__file__)
        ruta_carpeta_archivos = os.path.join(ruta_carpeta_script,"archivos")
        
        os.makedirs(fr"{ruta_carpeta_archivos}\{area}\{cargo}\{nombre_completo}", exist_ok=True)
        ruta_carpeta_persona  = os.path.abspath(os.path.join(ruta_carpeta_archivos,area,cargo,nombre_completo))
        print(ruta_carpeta_persona)
        ruta_archivo_bucle= fr"{ruta_carpeta_persona}\{nombre_archivo}_{nombre_completo}.{tipo_archivo}" 

        try:
            with open(ruta_archivo_bucle ,"wb") as f:
                f.write(contenido)

        except Exception as e:
            errores.append({"no cargó el archivo":e})

        if nombre_archivo == 'Firma' and tipo_archivo == 'pdf':
            return jsonify({"mensaje":"La firma no puede ser formatyo PDF, DEBE SER IMAGEN"})

        if nombre_archivo == 'Firma':
            ruta_firma =  ruta_archivo_bucle
            #uso un replace pq mysql me elimina los '\' y los '\b' se mos cambia por un <?>
            ruta_firma_para_almacenaje= ruta_firma.replace('\\','-')
            conexion = obtener_conexion_bd()
            cursor = conexion.cursor()
            cursor.execute('update usuarios set ruta_firma =%s where usuarios.id=%s ',(ruta_firma_para_almacenaje,id_usuario,))
            conexion.commit()
            cursor.close()
            conexion.close()
            
    conexion = obtener_conexion_bd()
    cursor= conexion.cursor()
    cursor.execute("select estado_id from usuariosxestado WHERE usuariosxestado.id_usuario=%s",(id_usuario,))
    res = cursor.fetchone()
    cursor.close()
    conexion.close()
    
    if res[0] == 2:
        from firma_fomatos.firma_documentos import Firma_documentos
        firma =Firma_documentos(nombre_completo,direccion,cedula,correo_electronico,telefono,area,cargo,tipo_sangre,fecha_nacimiento, ruta_carpeta_persona, ruta_firma)
        conexion = obtener_conexion_bd()
        cursor = conexion.cursor()
        cursor.execute('select ruta_firma from usuarios where id=%s',(id_usuario,))
        res = cursor.fetchone()
        cursor.close()
        conexion.close()
        
        if res[0] == None:
            return jsonify({"mensaje":"La firma es de caracter oblogatorio"}),400
        conexion = obtener_conexion_bd()
        cursor=conexion.cursor()
        cursor.execute("select estado_firma from usuarios where id=%s",(id_usuario,))
        res = cursor.fetchone()
        print(res)
        cursor.close()
        conexion.close()
        

        #si no ah firmado
        if res[0] == 0 or res[0]== None:
            print("entro al estado firma")
            print(type(cargo_id))
            if cargo_id == '1':
                firma.firmar_formatos_antibiotico()
            conexion = obtener_conexion_bd()
            cursor = conexion.cursor()
            cursor.execute("update usuarios set estado_firma=1 where id =%s", (id_usuario,))
            conexion.commit()
            cursor.close()
            conexion.close()
            

     #Firma de los formatos posterior a subir la firma
    if errores:
       
        # elif cargo ==2

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
        print(columna)
    return jsonify({'retorno':retorno})

if __name__ == '__main__':  
    app.run(debug=True,  host= '0.0.0.0' ,port=5009)
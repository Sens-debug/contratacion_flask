from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.APIs.Bd_contratacion import ConexionContratacion
from datetime import date
Conexion_contratacion = ConexionContratacion()

@jwt_required()
def traer_todo():
    usuario = get_jwt_identity()
    data = Conexion_contratacion.traer_todo()
    return jsonify(usuario=usuario , recibido = data),201

@jwt_required()
def crear_usuario():
    jwt_id= get_jwt_identity()
    peticion = request.get_json()
    nombres = [peticion.get("primer_nombre"),peticion.get("segundo_nombre"),peticion.get("primer_apellido"),peticion.get("segundo_apellido")]
    credenciales = [peticion.get("nombre_usuario"),peticion.get("contraseña_usuario")]
    fechas_nacimiento=[peticion.get("fecha_nacimiento")["day"],peticion.get("fechanacieminto")["month"],peticion.get("fecha_nacimiento")["year"]]
    fecha_nacimiento_completa = date(fechas_nacimiento[2],fechas_nacimiento[1],fechas_nacimiento[0])
    direccion = peticion.get("Direccion_Residencia")
    cedula = peticion.get("Cedula_ciudadania")
    correo = peticion.get("Correo_electronico")
    telefono = peticion.get("Telefono")
    cargo_seleccionado_id = peticion.get("cargo_seleccionado") 
    tipo_sangre_seleccionado_id = peticion.get("tipo_sangre_seleccionado") 
    empresa_id = peticion.get("empresa")

    mensaje,saas = Conexion_contratacion.crear_usuario(nombres,credenciales,fecha_nacimiento_completa,direccion,cedula,correo,telefono,cargo_seleccionado_id,tipo_sangre_seleccionado_id,empresa_id)

    return jsonify(mensaje=mensaje, comprobacion=saas)

@jwt_required()
def obtener_cargo_solicitante():
    id_solicitante = get_jwt_identity()
    cargo_id,saas = Conexion_contratacion.obtener_cargo_x_id(id_solicitante)
    return jsonify(cargo_id=cargo_id, comprobacion = saas)

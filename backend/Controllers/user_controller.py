from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.APIs.Bd_contratacion import ConexionContratacion

Conexion_contratacion = ConexionContratacion()

@jwt_required()
def traer_todo():
    usuario = get_jwt_identity()
    data = Conexion_contratacion.traer_todo()
    return jsonify(usuario=usuario , recibido = data),201
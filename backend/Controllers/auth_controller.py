from flask import request,jsonify
from flask_jwt_extended import create_access_token,set_access_cookies
from backend.APIs.Bd_contratacion import ConexionContratacion

Conexion_contratacion = ConexionContratacion()

def login():
    peticion = request.get_json()
    #{estado} representa el valor SaaS
    #{mensaje} representa el retorno Query BD
    retorno,saas=Conexion_contratacion.verificar_inicio_sesion(peticion.get("usuario"),peticion.get("contraseña"))
    data =retorno[0]
    loguea = retorno[1]
    if not loguea:
        return jsonify({"data":data,
                        "loguea":loguea,
                        "boolean":saas})
    print(data.get("id"))
    token = create_access_token(identity=str(data.get("id")))
    respuesta =jsonify({"mensaje":"login exitoso",
                        "loguea":loguea,
                        })
    set_access_cookies(respuesta,token)
    return respuesta
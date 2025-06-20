from flask import Blueprint
from backend.Controllers.user_controller import (traer_todo
                                                 ,crear_usuario,
                                                 obtener_cargo_solicitante)

user_bp= Blueprint('user',__name__)

user_bp.route('/traer_todo',methods=["GET"])(traer_todo)

user_bp.route('/crear_usuario',methods=["POST"])(crear_usuario)

user_bp.route('/obtener_cargo_id',methods=["POST"])(obtener_cargo_solicitante)
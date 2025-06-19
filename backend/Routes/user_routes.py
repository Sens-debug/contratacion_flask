from flask import Blueprint
from backend.Controllers.user_controller import traer_todo

user_bp= Blueprint('user',__name__)

user_bp.route('/traer_todo',methods=["GET"])(traer_todo)
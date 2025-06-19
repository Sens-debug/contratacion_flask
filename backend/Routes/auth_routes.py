from flask import Blueprint
from backend.Controllers.auth_controller import login

auth_bp = Blueprint('auth',__name__)

#Ruta login
auth_bp.route('/login', methods=['POST'])(login)

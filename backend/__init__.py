from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from backend.Middlewares.Config.jwt_config import configure_jwt
from backend.Routes.auth_routes import auth_bp
from backend.Routes.user_routes import user_bp

def crear_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)  # Habilita peticiones desde el frontend (React)

    # Configuración JWT
    configure_jwt(app)
    jwt = JWTManager(app)

    # Registro de blueprints (módulos de rutas)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    
    return app
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from backend.Middlewares.Config.jwt_config import configure_jwt
from backend.Routes.auth_routes import auth_bp
from backend.Routes.user_routes import user_bp

app = Flask(__name__)
CORS(app)  # Habilita peticiones desde el frontend (React)

# Configuración JWT
configure_jwt(app)
jwt = JWTManager(app)

# Registro de blueprints (módulos de rutas)
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='7800',debug=True)
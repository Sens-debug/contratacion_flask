from datetime import timedelta

def configure_jwt(app):
    app.config['JWT_SECRET_KEY'] = 'clave-super-secreta'
    app.config['JWT_TOKEN_LOCATION']={'cookies'}
    app.config['JWT_COOKIE_SECURE']=False
    app.config['JWT_COOKIE_HTTPONLY']=True
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)
    app.config['JWT_COOKIE_SAMESITE']= None
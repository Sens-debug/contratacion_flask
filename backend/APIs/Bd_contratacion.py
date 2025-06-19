import mysql.connector
from backend.Middlewares.SaaS.Saas import saas


class ConexionContratacion(mysql.connector.MySQLConnection):
    def __init__(self):
        config={
            'host':'localhost',
            'user':'root',
            'password':'',
            'database':'try_contratacion'
        }
        super().__init__(**config)
    
    def revisar_conexion(funcion_envuelta):
        '''Funcion Decoradora\n
        Si la conexion está cerrada, la re-abre con la misma configuracion de la instacian\n
        Comprueba el SaaS'''
        def envoltura(self,*args,**kwargs):
            control = saas()
            if not self.is_connected():
                self.connect()
            resultado = funcion_envuelta(self,*args,**kwargs)
            self.disconnect()
            return resultado, control
        return envoltura
        
    @revisar_conexion
    def verificar_inicio_sesion(self,usuario,contraseña):
        '''Retorna 2 valores Array->[ ( {Json} o string ), Boolean] y Boolean(SaaS) \n
        Json contiene {'id':{id} }\n
        String contiene el  mensaje, o errores\n
        Recibe Usuario y Contraseña'''
        try:
            with self.cursor(dictionary=True) as cursor:
                cursor.execute("select id from usuarios where nombre_usuario =%s and contraseña_usuario= %s",
                               (usuario,contraseña)
                               )
                resultados = cursor.fetchall()
                print(cursor.fetchall())
                id_usuario= resultados[0] if resultados else False
                if not id_usuario:
                    cursor.close()
                    return "Denegado", False
                cursor.close()
                return id_usuario, True
        except Exception as e:
            return e, False

    @revisar_conexion
    def traer_todo(self):
        with self.cursor(dictionary=True) as cursor:
            cursor.execute("select * from usuarios")
            datos = cursor.fetchall()
            cursor.close()
            return datos

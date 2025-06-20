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
                cursor.execute("select id,cargo_id from usuarios where nombre_usuario =%s and contraseña_usuario= %s",
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

    @revisar_conexion
    def crear_usuario(self,l_nombres,l_credenciales,fecha_nacimiento_completa,direccion,cedula,correo,telefono,cargo_id,tipo_sangre_seleccionado_id,empresa_id):
        try:
            with self.cursor() as cursor:
                cursor.execute("""INSERT INTO usuarios
                               (id,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,
                                direccion_residencia,cedula_ciudadania,correo_electronico,
                                cargo_id,tipo_sangre_id,telefono,ruta_firma,nombre_usuario,contraseña_usuario,empresa_id,fecha_nacimiento,estado_firma) 
                                VALUES
                                (%s,%s,%s,%s,%s,
                                    %s,%s,%s,
                                    %s,%s,%s,%s,
                                    %s,%s,%s,%s,%s);""",(None,l_nombres[0],l_nombres[1],l_nombres[2],l_nombres[3],
                                                 direccion,cedula,correo,
                                                 cargo_id,tipo_sangre_seleccionado_id,telefono,None,
                                                 l_credenciales[0],l_credenciales[1],empresa_id,fecha_nacimiento_completa,0 ))
                self.commit()
                cursor.execute("select id from usuarios where cedula_ciudadania =%s",(cedula,))
                id_usuario = cursor.fetchone()
                cursor.execute("""INSERT INTO usuariosxestado (id_usuario,estado_id) VALUES (%s,%s)""",(id_usuario[0],1))
                self.commit()
                cursor.close()
                return "Usuario Creado Exitosamente"
        except Exception as e:
            cursor.close()
            return "Error en la creacion de Usuario"

    @revisar_conexion
    def obtener_cargo_x_id(self,id):
        '''Devuelve String y Boolean\n
        String es el (Cargo_Id o Error) y Boolean es el SaaS'''
        try:
            with self.cursor() as cursor:
                cursor.execute("select cargo_id from usuarios where id=%s",(id,))
                data = cursor.fetchall[0][0]
                cursor.close()
                return data
        except Exception as e:
            cursor.close()
            return e
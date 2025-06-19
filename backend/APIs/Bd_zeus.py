import pymssql

class ConexionZeus:
    def __init__(self, server, user, password, database):
        self._config = {
            'server': server,
            'user': user,
            'password': password,
            'database': database
        }
        self.conexion = pymssql.connect(**self._config)

    def fetch_SaaS(self):
        '''Retorna 2 valores [Array] y Boolean
        Busca los registros del usuario SaaS'''
        try:
            self.reconectar()
            msjs = []
            with self.conexion.cursor() as cur:
                cur.execute("select id from usuario where id=1188")
                respuesta = cur.fetchall()
                if not respuesta:
                    msjs.append("No user")
                    return msjs,False
                msjs.append("Ok")
                return msjs,True
        except Exception as e:
            print(e)
            raise Exception

    def reconectar(self):
        try:
            self.conexion.close()
        except:
            pass  # Silenciar si ya está cerrada

        # Volver a conectar usando los mismos datos
        self.conexion = pymssql.connect(**self._config)

        print("Reconectado exitosamente.")

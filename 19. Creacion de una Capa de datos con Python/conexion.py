from logger_base import log
import psycopg2 as bd
import sys

# Definimos la clase Conexion para manejar la conexión a una base de datos PostgreSQL.
class Conexion:
    _DATABASE = 'test_db'        # Nombre de la base de datos.
    _USERNAME = 'postgres'       # Nombre de usuario para acceder a la base de datos.
    _PASSWORD = 'admin'          # Contraseña para acceder a la base de datos.
    _DB_PORT = '5432'            # Puerto para la conexión a la base de datos.
    _HOST = '127.0.0.1'          # Dirección del host donde se encuentra la base de datos.
    _conexion = None             # Variable para almacenar la conexión.
    _cursor = None               # Variable para almacenar el cursor.

    # Método de clase para obtener la conexión a la base de datos.
    @classmethod
    def obtenerConexion(cls):
        # Si la conexión no existe, la creamos.
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._DB_PORT,
                                           database=cls._DATABASE)
                log.debug(f'Conexión exitosa: {cls._conexion}')  # Registramos la conexión exitosa.
                return cls._conexion                            # Devolvemos la conexión.
            except Exception as e:                              # Si ocurre una excepción...
                log.error(f'Ocurrió una excepción al obtener la conexión: {e}')  # Registramos el error.
                sys.exit()                                      # Terminamos el programa.
        else:
            return cls._conexion                                # Si la conexión ya existe, la devolvemos.

    # Método de clase para obtener el cursor de la base de datos.
    @classmethod
    def obtenerCursor(cls):
        # Si el cursor no existe, lo creamos.
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Se abrió correctamente el cursor: {cls._cursor}')  # Registramos que el cursor se abrió correctamente.
                return cls._cursor                                           # Devolvemos el cursor.
            except Exception as e:                                           # Si ocurre una excepción...
                log.error(f'Ocurrió una excepción al obtener el cursor: {e}')  # Registramos el error.
                sys.exit()                                                    # Terminamos el programa.
        else:
            return cls._cursor                                                # Si el cursor ya existe, lo devolvemos.

# Bloque principal para ejecutar los métodos y probar la conexión y el cursor.
if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()

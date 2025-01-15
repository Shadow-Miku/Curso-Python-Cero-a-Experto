from logger_base import log
from psycopg2 import pool
import sys

# Definimos la clase Conexion para manejar la conexión a una base de datos PostgreSQL usando un pool de conexiones.
class Conexion:
    _DATABASE = 'test_db'  # Nombre de la base de datos.
    _USERNAME = 'postgres'  # Nombre de usuario para acceder a la base de datos.
    _PASSWORD = 'admin'  # Contraseña para acceder a la base de datos.
    _DB_PORT = '5432'  # Puerto para la conexión a la base de datos.
    _HOST = '127.0.0.1'  # Dirección del host donde se encuentra la base de datos.
    _MIN_CON = 1  # Número mínimo de conexiones en el pool.
    _MAX_CON = 5  # Número máximo de conexiones en el pool.
    _pool = None  # Variable para almacenar el pool de conexiones.

    # Método de clase para obtener el pool de conexiones.
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:  # Si el pool no existe, lo creamos.
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f'Creación del pool exitosa: {cls._pool}')  # Registramos la creación exitosa del pool.
                return cls._pool  # Devolvemos el pool.
            except Exception as e:  # Si ocurre una excepción...
                log.error(f'Ocurrió un error al obtener el pool {e}')  # Registramos el error.
                sys.exit()  # Terminamos el programa.
        else:
            return cls._pool  # Si el pool ya existe, lo devolvemos.

    # Método de clase para obtener una conexión del pool.
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida del pool: {conexion}')  # Registramos la conexión obtenida.
        return conexion

    # Método de clase para liberar una conexión y devolverla al pool.
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexión al pool: {conexion}')  # Registramos la devolución de la conexión.

    # Método de clase para cerrar todas las conexiones del pool.
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()

# Bloque principal para probar la obtención y liberación de conexiones.
if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion5)
    conexion6 = Conexion.obtenerConexion()

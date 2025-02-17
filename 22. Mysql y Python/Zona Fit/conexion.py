import mysql.connector
from mysql.connector import pooling

class Conexion:
    DATABASE = "zona_fit_db"
    USERNAME = "root"
    PASSWORD = ""
    PORT = "3306"
    HOST = "localhost"
    POOL_SIZE = 5
    POOL_NAME = "zona_fit_pool"
    pool = None

    @classmethod
    def get_pool(cls):
        """
        Crea y devuelve una conexión a la pool de MySQL.
        Si la pool ya existe, devuelve la pool existente.
        """
        if cls.pool is None:  # Si la pool no ha sido creada, lo creamos
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.PORT,
                    user=cls.USERNAME,
                    password=cls.PASSWORD,
                    database=cls.DATABASE
                )
                #print(f'Nombre de la pool: {cls.POOL_NAME}, Tamaño de la pool: {cls.POOL_SIZE}')
            except mysql.connector.Error as err:
                print(f"Error al crear la pool: {err}")
                return None
        return cls.pool

    @classmethod
    def obtener_conexion(cls):
        """
        Obtiene una conexión desde la pool.
        """
        try:
            return cls.get_pool().get_connection()
        except mysql.connector.Error as err:
            print(f"Error al obtener la conexión: {err}")
            return None

    @classmethod
    def liberar_conexion(cls, conexion):
        """
        Cierra y libera una conexión de vuelta a la pool.
        """
        try:
            conexion.close()
        except mysql.connector.Error as err:
            print(f"Error al liberar la conexión: {err}")

if __name__ == "__main__":
    pool = Conexion.get_pool()
    if pool is not None:
        print("Conexión a la pool exitosa")
    else:
        print("Error al obtener la pool")

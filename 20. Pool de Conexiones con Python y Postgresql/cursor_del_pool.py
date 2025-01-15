from logger_base import log
from conexion import Conexion

# Definimos la clase CursorDelPool para manejar automáticamente la obtención y liberación de conexiones y cursores de la base de datos.
class CursorDelPool:
    def __init__(self):
        self._conexion = None  # Variable para almacenar la conexión.
        self._cursor = None  # Variable para almacenar el cursor.

    # Método especial __enter__ para el manejo del contexto with.
    def __enter__(self):
        log.debug('Incio del método with __enter__')
        self._conexion = Conexion.obtenerConexion()  # Obtiene una conexión del pool.
        self._cursor = self._conexion.cursor()  # Obtiene un cursor de la conexión.
        return self._cursor  # Retorna el cursor.

    # Método especial __exit__ para el manejo del contexto with.
    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug('Se ejecuta método __exit__')
        if valor_excepcion:  # Si ocurrió una excepción...
            self._conexion.rollback()  # Realiza rollback de la transacción.
            log.error(f'Ocurrió una excepción, se hace rollback: {valor_excepcion} {tipo_excepcion} {detalle_excepcion}')  # Registra el error.
        else:
            self._conexion.commit()  # Realiza commit de la transacción.
            log.debug('Commit de la transacción')
        self._cursor.close()  # Cierra el cursor.
        Conexion.liberarConexion(self._conexion)  # Libera la conexión y la devuelve al pool.

# Bloque principal para probar el manejo de contexto con CursorDelPool.
if __name__ == '__main__':
    with CursorDelPool() as cursor:  # Inicia un bloque with utilizando CursorDelPool.
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM persona')  # Ejecuta una consulta SQL.
        log.debug(cursor.fetchall())  # Registra los resultados de la consulta.

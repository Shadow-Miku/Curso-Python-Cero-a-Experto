from conexion import Conexion
from persona import Persona
from logger_base import log

# Definimos la clase PersonaDAO para manejar las operaciones de la base de datos relacionadas con la tabla "persona".
class PersonaDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create-Read-Update-Delete)
    '''
    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'  # Consulta para seleccionar todas las personas ordenadas por id_persona.
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'  # Consulta para insertar una nueva persona.
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'  # Consulta para actualizar una persona existente.
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'  # Consulta para eliminar una persona.

    # Método de clase para seleccionar todas las personas de la base de datos.
    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas

    # Método de clase para insertar una nueva persona en la base de datos.
    @classmethod
    def insertar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'Persona insertada: {persona}')
                return cursor.rowcount  # Devuelve el número de filas insertadas.

    # Método de clase para actualizar una persona existente en la base de datos.
    @classmethod
    def actualizar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email, persona.id_persona)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Persona actualizada: {persona}')
                return cursor.rowcount  # Devuelve el número de filas actualizadas.

    # Método de clase para eliminar una persona de la base de datos.
    @classmethod
    def eliminar(cls, persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Objeto eliminado: {persona}')
                return cursor.rowcount  # Devuelve el número de filas eliminadas.

# Bloque principal para probar las operaciones CRUD.
if __name__ == '__main__':
    # Insertar un registro (comentado para evitar ejecución automática).
    # persona1 = Persona(nombre='Pedro', apellido='Najera', email='pnajera@mail.com')
    # personas_insertadas = PersonaDAO.insertar(persona1)
    # log.debug(f'Personas insertadas: {personas_insertadas}')

    # Actualizar un registro (comentado para evitar ejecución automática).
    # persona1 = Persona(1,'Juan Carlos', 'Juarez', 'cjjuarez@mail.com')
    # personas_actualizadas = PersonaDAO.actualizar(persona1)
    # log.debug(f'Personas actualizadas: {personas_actualizadas}')

    # Eliminar un registro.
    persona1 = Persona(id_persona=20)
    personas_eliminadas = PersonaDAO.eliminar(persona1)
    log.debug(f'Personas eliminadas: {personas_eliminadas}')

    # Seleccionar y mostrar todas las personas.
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)

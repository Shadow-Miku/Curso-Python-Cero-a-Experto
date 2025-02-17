from conexion import Conexion
from cliente import Cliente

class ClienteDAO:
    """
    Data Access Object para la clase Cliente.
    Proporciona métodos para realizar operaciones CRUD en la base de datos.
    """
    SELECCIONAR = "SELECT * FROM cliente"
    INSERTAR = "INSERT INTO cliente (nombre, apellido, membresia) VALUES (%s, %s, %s)"
    ACTUALIZAR = "UPDATE cliente SET nombre = %s, apellido = %s, membresia = %s WHERE id = %s"
    ELIMINAR = "DELETE FROM cliente WHERE id = %s"

    @classmethod
    def seleccionar(cls):
        """
        Selecciona todos los registros de la tabla cliente.
        
        Retorna:
            List[Cliente]: Lista de objetos Cliente.
        """
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f"No se pudo obtener la conexión, error: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        """
        Inserta un nuevo registro en la tabla cliente.
        
        Parámetros:
            cliente (Cliente): El objeto Cliente a insertar.
            
        Retorna:
            int: Número de registros insertados.
        """
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"No se pudo obtener la conexión, error: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        """
        Actualiza un registro existente en la tabla cliente.
        
        Parámetros:
            cliente (Cliente): El objeto Cliente con los nuevos datos.
            
        Retorna:
            int: Número de registros actualizados.
        """
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"No se pudo obtener la conexión, error: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        """
        Elimina un registro de la tabla cliente.
        
        Parámetros:
            cliente (Cliente): El objeto Cliente a eliminar.
            
        Retorna:
            int: Número de registros eliminados.
        """
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"No se pudo obtener la conexión, error: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == "__main__":
    # Insertar un nuevo cliente
    # cliente = Cliente(nombre="Juan", apellido="Perez", membresia="10201")
    # print(f"Se insertaron {ClienteDAO.insertar(cliente)} registros")

    # Actualizar un cliente existente
    # cliente_Actualizar = Cliente(8, "ACTUALIZADO", "ACTUALIZADO", "40")
    # print(f"Se actualizaron {ClienteDAO.actualizar(cliente_Actualizar)} registros")

    # Eliminar un cliente existente
    #cliente_Eliminar = Cliente(id=8)
    #clientes_eliminados = ClienteDAO.eliminar(cliente_Eliminar)
    #print(f"Se elimino: {clientes_eliminados}")

    # Seleccionar todos los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)

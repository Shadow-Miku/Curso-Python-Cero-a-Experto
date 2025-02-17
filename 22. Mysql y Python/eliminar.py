import mysql.connector

# Conexión a la base de datos
mydb = mysql.connector.connect(
    host="localhost",  # Nombre del host
    user="root",  # Nombre de usuario de la base de datos
    password="",  # Contraseña del usuario de la base de datos
    database="repasodb"  # Nombre de la base de datos
)

# Creación del cursor para ejecutar consultas
mycursor = mydb.cursor()

sentencia_sql = "DELETE FROM books WHERE id = %s"

try:
    # Ejecuta la sentencia SQL con el valor proporcionado
    mycursor.execute(sentencia_sql, (4,))
    # Confirma (commit) la transacción a la base de datos
    mydb.commit()
    # Imprime el número de registros eliminados
    print(mycursor.rowcount, "registro(s) eliminado(s)")
except mysql.connector.Error as err:
    # Captura y muestra cualquier error que ocurra durante la ejecución de la consulta
    print("Error: {}".format(err))
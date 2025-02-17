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

# Sentencia SQL para actualizar registros en la tabla 'books'
sentencia_sql = "UPDATE books SET title = %s, author = %s, publisher = %s, year = %s, isbn = %s, price = %s, updated_at = NOW() WHERE id = %s"

# Valores a actualizar
valores = ("La Frescura de la Tierra", "A. R. Nieves", "Pavlov", 2001, "0-395-19395-8", 22.99, 3)

try:
    # Ejecuta la sentencia SQL con los valores proporcionados
    mycursor.execute(sentencia_sql, valores)
    # Confirma (commit) la transacción a la base de datos
    mydb.commit()
    # Imprime el número de registros actualizados
    print(mycursor.rowcount, "registro(s) actualizado(s)")
except mysql.connector.Error as err:
    # Captura y muestra cualquier error que ocurra durante la ejecución de la consulta
    print("Error: {}".format(err))

# Cierra el cursor y la conexión a la base de datos
mycursor.close()
mydb.close()

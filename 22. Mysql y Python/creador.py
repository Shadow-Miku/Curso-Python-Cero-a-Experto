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

# Sentencia SQL para insertar registros en la tabla 'books'
sentencia_sql = "INSERT INTO books (title, author, publisher, year, isbn, price, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, NOW(), NOW())"

# Tupla de valores a insertar
valores = [
    ("The Lord of the Rings", "J. R. R. Tolkien", "Allen & Unwin", 1954, "0-395-19395-8", 22.99),
    ("The Hobbit", "J. R. R. Tolkien", "Allen & Unwin", 1937, "0-395-19395-8", 19.99),
    ("The Silmarillion", "J. R. R. Tolkien", "Allen & Unwin", 1977, "0-395-19395-8", 15.99)
]

try:
    # Ejecuta la sentencia SQL con múltiples valores
    mycursor.executemany(sentencia_sql, valores)
    # Confirma (commit) la transacción a la base de datos
    mydb.commit()
    # Imprime el número de registros insertados
    print(mycursor.rowcount, "registro(s) insertado(s)")
except mysql.connector.Error as err:
    # Captura y muestra cualquier error que ocurra durante la ejecución de la consulta
    print("Error: {}".format(err))

# Cierra la conexión a la base de datos
mydb.close()

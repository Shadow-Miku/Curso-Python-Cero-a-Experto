import mysql.connector

# Conectar a la base de datos
mydb = mysql.connector.connect(
    host="localhost",  # Nombre del host donde se encuentra la base de datos
    user="root",  # Nombre de usuario de la base de datos
    password="",  # Contraseña del usuario de la base de datos
    database="repasodb"  # Nombre de la base de datos
)

# Crear un cursor para ejecutar las consultas
mycursor = mydb.cursor()

# Seleccionar el título y el autor de todos los libros de la tabla 'books'
mycursor.execute("SELECT title, author FROM books")

# Obtener todos los resultados de la consulta
myresult = mycursor.fetchall()

# Iterar sobre los resultados y mostrarlos
for titulo, autor in myresult:
    print(f"Título: {titulo}, Autor: {autor}")

# Cerrar el cursor y la conexión a la base de datos
mycursor.close()
mydb.close()

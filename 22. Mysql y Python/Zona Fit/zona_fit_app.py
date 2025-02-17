from cliente import Cliente
from clienteDAO import ClienteDAO

print("*** Clientes de zona fit (GYM) ***")
option = None

while option != 5:
    print("1. Listar clientes")
    print("2. Agregar clientes")
    print("3. Actualizar clientes")
    print("4. Eliminar clientes")
    print("5. Salir")
    option = int(input("Ingrese una opción 1 a 5: "))

    if option == 1:
        clientes = ClienteDAO.seleccionar()
        print('\n *** Listado de clientes ***')
        for cliente in clientes:
            print(cliente)
        print('\n')

    elif option == 2:
        nombre_var = input("Ingrese el nombre del cliente: ")
        apellido_var = input("Ingrese el apellido del cliente: ")
        membresia_var = input("Ingrese el tipo de membresía del cliente: ")
        cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        clientes_insertados = ClienteDAO.insertar(cliente)
        print(f"Se insertaron {clientes_insertados} registros")

    elif option == 3:
        id_cliente_var = int(input("Ingrese el ID del cliente: "))
        nombre_var = input("Ingrese el nombre del cliente: ")
        apellido_var = input("Ingrese el apellido del cliente: ")
        membresia_var = input("Ingrese el tipo de membresía del cliente: ")
        cliente = Cliente(id=id_cliente_var, nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        clientes_actualizados = ClienteDAO.actualizar(cliente)
        print(f"Se actualizaron {clientes_actualizados} registros")

    elif option == 4:
        id_cliente_var = int(input("Ingrese el ID del cliente a eliminar: "))
        cliente = Cliente(id=id_cliente_var)
        clientes_eliminados = ClienteDAO.eliminar(cliente)
        print(f"Se eliminaron {clientes_eliminados} registros")

    elif option == 5:
        print("Hasta pronto...")
    else:
        print("Opción no válida")

class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        """
        Inicializa una nueva instancia de la clase Cliente.

        Parámetros:
        id (int): El ID del cliente.
        nombre (str): El nombre del cliente.
        apellido (str): El apellido del cliente.
        membresia (str): El tipo de membresía del cliente.
        """
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia
        
    def __str__(self):
        """
        Devuelve una representación en cadena del objeto Cliente.

        Retorna:
        str: Una cadena que describe al cliente.
        """
        return f"ID: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Membresia: {self.membresia}"

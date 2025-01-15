from logger_base import log

# Definimos la clase Persona para representar una persona con sus atributos y métodos.
class Persona:
    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self._id_persona = id_persona  # Inicializa el atributo id_persona.
        self._nombre = nombre          # Inicializa el atributo nombre.
        self._apellido = apellido      # Inicializa el atributo apellido.
        self._email = email            # Inicializa el atributo email.

    # Método especial para retornar una representación en cadena de la instancia.
    def __str__(self):
        return f'''
            Id Persona: {self._id_persona}, Nombre: {self._nombre},
            Apellido: {self._apellido}, Email: {self._email}
        '''

    # Propiedad para obtener el valor de id_persona.
    @property
    def id_persona(self):
        return self._id_persona

    # Propiedad para establecer el valor de id_persona.
    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    # Propiedad para obtener el valor de nombre.
    @property
    def nombre(self):
        return self._nombre

    # Propiedad para establecer el valor de nombre.
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Propiedad para obtener el valor de apellido.
    @property
    def apellido(self):
        return self._apellido

    # Propiedad para establecer el valor de apellido.
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    # Propiedad para obtener el valor de email.
    @property
    def email(self):
        return self._email

    # Propiedad para establecer el valor de email.
    @email.setter
    def email(self, email):
        self._email = email

# Bloque principal para probar la creación de objetos Persona y los registros de depuración.
if __name__ == '__main__':
    # Crear un objeto Persona con todos los atributos.
    persona1 = Persona(1, 'Juan', 'Perez', 'jperez@mail.com')
    log.debug(persona1)  # Registra el objeto Persona creado.

    # Simular un insert creando un objeto Persona sin id_persona.
    persona1 = Persona(nombre='Juan', apellido='Perez', email='jperez@mail.com')
    log.debug(persona1)  # Registra el objeto Persona creado.

    # Simular un delete creando un objeto Persona solo con id_persona.
    persona1 = Persona(id_persona=1)
    log.debug(persona1)  # Registra el objeto Persona creado.

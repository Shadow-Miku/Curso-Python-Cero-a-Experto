import logging as log

# Configuración básica del módulo de logging.
log.basicConfig(level=log.DEBUG,  # Establece el nivel de registro a DEBUG.
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',  # Define el formato del mensaje de registro.
                datefmt='%I:%M:%S %p',  # Define el formato de la fecha y hora.
                handlers=[
                    log.FileHandler('capa_datos.log'),  # Registra los mensajes en un archivo llamado 'capa_datos.log'.
                    log.StreamHandler()  # Muestra los mensajes en la consola.
                ])

# Bloque principal para probar los diferentes niveles de registro.
if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')  # Registro de un mensaje a nivel DEBUG.
    log.info('Mensaje a nivel info')  # Registro de un mensaje a nivel INFO.
    log.warning('Mensaje a nivel de warning')  # Registro de un mensaje a nivel WARNING.
    log.error('Mensaje a nivel de error')  # Registro de un mensaje a nivel ERROR.
    log.critical('Mensaje a nivel critico')  # Registro de un mensaje a nivel CRITICAL.

# Contador de vocales en python

print('*** Contador de vocales ***')
ingresa_palabra = input('Ingresa una palabra: ')

# Contador de vocales
vocales = 'aeiouAEIOU'

# Contador de vocales
cont_vocales = 0

for vocal in ingresa_palabra:
    if vocal in vocales:
        cont_vocales += 1

print(f'La palabra {ingresa_palabra} tiene {cont_vocales} vocales')
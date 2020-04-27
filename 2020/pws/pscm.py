#!/usr/bin/env python3
'''Strings warm-up'''

# format

saludo = 'hola'
despido = 'chao'
print('Yo saludo con \'{}\' y me despido con \'{}\''.format(saludo, despido))
print('+'*5)
print(f'Yo saludo con {saludo} y me despido con {despido}')
print('*'*5)

print(saludo.upper())
print(saludo.capitalize())
print(saludo.count('a'))
print('*'*5)

nombre = input('Como te llamas? ')
print(f'Tu nombre es {nombre}')
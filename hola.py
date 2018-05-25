#!/usr/bin/python3

# Este programa dice hola y te pregunta el nombre

print('hola mundo!')
print('Cual es tu nombre?')
myNombre = input()
print('Gusto con conocer, ' + myNombre)
print('El numero de letra en tu numbre es:')
print(len(myNombre))
print('Que edad tienes?')
myEdad = input()
print('Tu tines ' + str(int(myEdad)) + ' anios.')

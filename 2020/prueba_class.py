#!/usr/bin/env python3


# Author: Jose Apablaza
# Purpose: Test the Python Class


class miclase:
    variable = 'Hola'

    def mensaje(self):
        print('Primera prueba')


print(miclase.variable)

obj1 = miclase()
obj2 = miclase()

obj2.variable = 'Hello'

print(obj1.variable)
print(obj2.variable)

obj1.mensaje()
miclase().mensaje()

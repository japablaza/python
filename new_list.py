#!/usr/bin/python3

# Lista original
list = [6,4,2]
print('Lista de numeros originales')
print(list)

# Agregando 12, 8 y 4
list.extend((12,8,4))

# Lista original con los nuevos numeros
print('Lista de numeros mas 12, 4 y 8')
print(list)

# Cambio de valos en segundo item de la lista 
list[1] = 3
print('Lista original con el segundo item actualizado')
print(list)

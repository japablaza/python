#!/usr/bin/python3

# Ejercicio tomado desde pythonbasics.org/split

punto = " Todo vamos al cielo. Pero algunos van donde quieren. El resto quien sabe. Fin."
oracion = punto.split('.')
print(oracion)

# El largo de cada oracion
print("Primera oracion")
print(len(oracion[0]))

print("Segunda oracion")
print(len(oracion[1]))

print("Tercera oracion")
print(len(oracion[2]))

print("Cuarta oracion")
print(len(oracion[3]))

print("Quinta oracion")
print(len(oracion[4]))

# El largo de la oracion completa
print(len(punto))

for x in oracion:
 print(x)
 print(" Numero total de caracteres: " + str(len(x)))

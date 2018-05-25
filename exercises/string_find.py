#!/usr/bin/python3

a = ("No tengo idea cuantos caracteres tienes esta oracion, esta, esta")
print(a)

if "idea" in a:
 print("Esa palabra existe")
else:
 print("la palabra idea no se encuentra")

print("Encuentra la posicion de la palabra -esta-: ")
c = input()

b = a.find("c")

print("La palabra que buscas se encuentra en la posicion: " + str(b)) 

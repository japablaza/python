#!/usr/bin/python3

# Replace() method. The first parameter is the word to search, the second parameter specifies the new value.
# The output needs to be saved in the strig.

t = "Hola mundo"
j = t.replace("mundo","Jose")
print(j)

# Optional parameter is the number of items that will be replaced.

a = ("Hola mundo mundo mundo")
b = a.replace("mundo","Jose",1)
print(b)

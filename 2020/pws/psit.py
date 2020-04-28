#!/usr/bin/env python3
'''Warm-up with string index'''

texto = 'Las mujeres no olvida, archivan'
frase = 'La verdad absoluta no existe'

print(texto[1])
print(texto[4:9])
print(frase[-6:])

## Boolean
a, b , c, d = True, True, False, False
ab = a and b
ac = a and c
cd = c and d

orab = a or b
orac = a or c
orcd = c or d

print(ab, ac, cd)
print(orab, orac, orcd)
print(a < b)
print(a > b)
print(a <= b)

# edad = input('Que edad tienes? ')
# if int(edad) >= 66:
#     print(texto)
# else:
#     print(frase)

edad = input('Que edad tienes? ')
edad = int(edad)
if edad < 10:
    print('Have a fun day!!')
elif edad >=10 and edad < 18:
    print('Almost there')
elif edad >= 18 and edad < 21:
    print('Ready for the army')
    print('Still a baby for beer')
elif edad == 21:
    print('Ready for a bright future!')
else:
    print('Too old')
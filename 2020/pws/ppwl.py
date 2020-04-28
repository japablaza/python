#!/usr/bin/env python3
'''loops'''

n = 0
while n < 5:
    print(f'number: {n}')
    n += 1  

n = 1

while n < 100:
    if n % 19 == 0:
        print(f'El numero {n} es el primer numero que se divide por 19')
        break
    n += 1

n = 1
tf = 24
ts = 36
while n < 100:
    if n % tf == 0 and n % ts == 0:
        print(f'Los numeros {tf} y {ts} son divisibles for {n}')
        break
    n += 1

print('+' * 20)

## The loop #
numero = abs((int(input('Dame un numero y busquemos si es un cuadrado perfecto: '))))

n = -1
cuadrado = False
while n <= numero**(0.5):
    n += 1
    if n*n == numero:
        cuadrado = True
        break
if cuadrado:
    print(f'El cuadrado de {numero} es {n}.')
else:
    (f'El numero {numero} no tiene un cuadrado perfecto')


## Second loop ##
arriendo = 350000
print('Una pieza en la costa: $350.000')
primera = abs(int(input('Cual es tu primera oferta: ')))
segunda = abs(int(input('Cual es tu segunda oferta: ')))
incremento = abs(int(input('Incremento: ')))

oferta_aceptada = False
while primera <= segunda:
    if primera >= arriendo:
        oferta_aceptada = True
        print(f'La oferta de {primera} fue aceptada!')
        break
    print(f'Lo sentimos, pero la ofereta de {primera}')
    primera += incremento
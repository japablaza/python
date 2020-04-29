#!/usr/bin/env python3
''' for-loop'''

for a in range(10):
    print(a)

texto = 'Vamos a la playa, oh oh oh!!'
for txt in texto:
    if txt == ' ':
        print('!!')
        continue
    print(txt)

for w in range(1, 10, 3):
    print(w)

n = 'loro'
for e in range(4):
    for e in n:
        print(e)
    print('Next')

for a in range(10, 100):
    if a % 2 == 0:
        continue
    if a % 3 == 0:
        continue
    if a % 5 == 0:
        continue
    if a % 7 == 0:
        continue
    print(a)

print('+'*20)
prim = [2, 3, 5, 7]
for q in range(10, 100):
    for p in prim:
        if q % p == 0:
            continue
        else:
            print(q)
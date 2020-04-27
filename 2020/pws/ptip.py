#!/usr/bin/env python3
'''This is activity 2'''

import math

x, y, z = 2, 3, 4

x_pow = math.pow(x, 2)
y_pow = math.pow(y, 2)
z_pow = math.pow(z, 2)

pow_list = [x, y, z]

xyz_pows = x_pow + y_pow + z_pow

sum_pow = 0
for b in pow_list:
    sum_pow = sum_pow + math.pow(b ,2)


escuare = math.sqrt(sum_pow)
print(escuare)
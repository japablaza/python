#!/usr/bin/env python

a = int(input("primer numero: "))
b = int(input("segundo numero: "))

a = a // b 
b = b // a

print(b)
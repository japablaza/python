#!/usr/bin/python

num1 = int(input("Dame el primer numero: "))
num2 = int(input("Dame el segundo numero: "))

if num1 % 4 == 0:
    print('Multiple of 4')
elif num1 % 2 == 0:
    print('Even number')
else:
    print('Odd number')
    
check = num1 % num2 

if check == 0:
    print("Even number")
else:
    print("Odd number")
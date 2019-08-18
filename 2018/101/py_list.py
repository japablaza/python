#!/usr/bin/python3

x = [3,4,5]
print('Esta es la lista original: ' + str(x))

x.append(7)
print('Esta es la lista original + 7: ' + str(x))

x.append(9)
print('Esta es la lista original + 7 y 9: ' + str(x))

x.pop()
print(x)

print(x[0])
print(x[1])

print(x[-1])

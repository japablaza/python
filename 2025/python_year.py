
year = int(input('Que anio se creo Python 1.0? '))

while year != 1994:
    if year < 1994:
        print('It was later than that!')
        year = int(input('When was Python 1.0 released? '))

    elif year > 1994:
        print('It was earlier than that!')
        year = int(input('When was Python 1.0 released? '))

print('Correct!')

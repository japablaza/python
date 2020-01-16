#!/usr/bin/env python3

# Purpose: Saludar
# Author: Jose Apablaza

import sys


def greet(name):
    return f'Hello, {name}!'


def test_greet():
    assert greet('World') == 'Hello, World!'
    assert greet('Mono') == 'Hello, Mono!'
    assert greet('Mundo') == 'Hello, Mundo!'


argumento = sys.argv[1:]
nombre = argumento[0] if argumento else 'Mundo'
print(greet(nombre))

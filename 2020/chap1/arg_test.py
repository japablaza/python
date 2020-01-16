#!/usr/bin/env python3

# Purpose: Learn Python 
# Author: Jose Apablaza

import sys


def saludo(name):
    return f'Hola, {name}!'


def test_saludo():
    assert saludo('Mundo') == 'Hola, Mundo!'
    assert saludo('Tierra Nueva') == 'Hola, Tierra Nueva!'


args = sys.argv[1:]
name = args[0] if args else 'World'
print(saludo(name))


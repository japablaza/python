#!/usr/bin/env python3

# Author: Jose Apablaza
# Purpose: Working witn Class

# Definir un objecto


class auto:
    nombre = 'Delorean'
    tipo = 'Maquina del tiempo'
    color = 'Plateado'
    valor = 800000000000000

    def descripcion(self):
        desc_str = 'El %s es una %s de color %s. Tiene un valor de $%.2f pesos.' % (self.nombre, self.tipo, self.color, self.valor)
        return desc_str


print(auto().descripcion())

auto1 = auto()
auto2 = auto()

auto1.nombre = 'Lada'
auto1.color = 'rojo'
auto1.tipo = 'convertible'
auto1.valor = 60000.00

print(auto1.descripcion())

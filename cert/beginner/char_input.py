#!/usr/bin/python

from datetime import datetime as dt
# Exercise https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# # Request user name and age
name = input("What's your name? ")
age  = int(input("Que edad tienes? "))
year = dt.now().year

diff_cien = 100 - age

new_age = diff_cien + year

print(f"{name.title()}, you will be 100 years old in {new_age}")
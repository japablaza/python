#!/usr/bin/python

text = 'Python is great'

new_text = text.split()
text_tuple = tuple(new_text)
print(f'Este es new_text: {new_text}, type: {type(new_text)}')
print(f'Este es text_tuple: {text_tuple}, type: {type(text_tuple)}')


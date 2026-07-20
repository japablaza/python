from ddgs import DDGS
from fastcore.all import *

def buscar_imagenes(keyword, max_images=200):
    return L(DDGS().images(keyword, max_results=max_images)).itemgot('image')


urls = buscar_imagenes('imagen de gatos', max_images=10) # Diccionario 
primeraImagenURL = urls[0]
print(primeraImagenURL)


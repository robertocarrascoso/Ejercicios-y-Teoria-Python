# 6. Crea una función generar_contraseña(longitud) que genere una contraseña aleatoria con letras, números y símbolos. En esta ocasión necesitas importar la libreria random. 

import random

def generar_contraseña(longitud):
    mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minusculas = "abcdefghijklmnopqrstuvwxyz"
    numeros = "0123456789"
    simbolos = "!#$%&'()*+,-./:;<=>?]@[^_`{|}~"
    
    caracteres = mayusculas + minusculas + numeros + simbolos
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    print(contraseña)

generar_contraseña(9)
generar_contraseña(6)

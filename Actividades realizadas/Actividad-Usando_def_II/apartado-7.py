# 7. Crea una función juego_adivina_numero() en la que el usuario intente adivinar un número aleatorio entre 1 y 100. Aquí también aplicas la libreria random + un bucle con el while. 

import random

def juego_adivina_numero():
    numero_aleatorio = random.randint(1, 100)
    
    while True:
        adivinanza = int(input("Adivina el número entre 1 y 100: "))
        intentos += 1
        
        if adivinanza < numero_aleatorio:
            print("Demasiado bajo. Intenta de nuevo.")
        elif adivinanza > numero_aleatorio:
            print("Demasiado alto. Intenta de nuevo.")
        else:
            break

juego_adivina_numero()

# 5. Crea una función contar_palabras(frase) que reciba un string y devuelva un diccionario con la frecuencia de cada palabra. Por ejemplo el resultado sería => "Hola"  :1, "Mundo": 2.


def contar_palabras(frase):
    palabras = frase.split()
    resultado = ""
    
    for orden in range(len(palabras)):
        if orden > 0:
            resultado += ", "
        resultado = ', '.join(f'"{palabra}": {orden+1}' for orden, palabra in enumerate(palabras))
    
    print(resultado)

contar_palabras("Hola Mundo tonto tonto tonto")
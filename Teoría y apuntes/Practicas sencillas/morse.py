# Código Roberto Carrascoso - 1ºA GM SMR
def morsecoder(palabra): # Creamos las traducciones de cada letra
    alfabeto = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-.."
    }
    
    resultado = ""
    for i in range(len(palabra)): # Creamos el proceso de traducción con el morsecoder
        resultado += alfabeto[palabra[i]] + "/" 
    print("La palabra", palabra, "en código morse es:") # Mostramos parte del resultado
    print(resultado) # Mostramos el resultado al completo
    
# Declaramos las palabras
palabra_1 = "hija"
palabra_2 = "bala"
palabra_3 = "gafa"
# Traducimos la palabra
morsecoder(palabra_1)
morsecoder(palabra_2)
morsecoder(palabra_3)
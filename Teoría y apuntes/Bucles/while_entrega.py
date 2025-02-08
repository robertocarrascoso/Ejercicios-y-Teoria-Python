#Código Estructura While con criterio de finalización
#Roberto Carrascoso Jordán
quit_prgm = "quit" #Palabra clave para salir

while True: #Bucle infinito hasta que se cumpla la condición
    entrada_inicial = input("Escribe algo: ")
    if entrada_inicial == quit_prgm: #Si el usuario escribe "quit", se termina el programa
        print("¡Adiós!")
        break #Terminamos el bucle
    else:
        print(entrada_inicial) #Mostramos el mensaje
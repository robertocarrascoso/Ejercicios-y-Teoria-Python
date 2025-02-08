# Roberto Carrascoso Jordán - 1ºCFGM SMR
# Actividad Leer Ficheros - v2

# La versión 1 fue corregida en clase y el profesor dijo que pedía eso.

# Esta versión v2 es la que se pide en el enunciado de la actividad bajo mi interpretación.
# Le he añadido el ".join(nombre_de_la_lista)" para que se muestre bien en terminal.

with open ("./hechos.txt", "r") as file:
    archivo = file.readlines()
    print("\nLo siguiente fue leído del archivo: hechos.txt\n")
    print("".join(archivo))
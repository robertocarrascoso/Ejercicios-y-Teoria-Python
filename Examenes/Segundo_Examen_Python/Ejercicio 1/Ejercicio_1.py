# Escribe un programa que abra un archivo llamado texto.txt y 
# lea todo su contenido utilizando el método read(). 
# Luego, imprime el contenido en la terminal.

with open("texto.txt", "r") as archivo:
    contenido = archivo.read()
print(contenido)
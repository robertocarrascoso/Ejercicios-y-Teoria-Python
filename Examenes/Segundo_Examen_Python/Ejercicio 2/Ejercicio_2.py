# Escribe un programa que lea un archivo llamado datos.txt 
# línea por línea utilizando el método readline(). 
# El programa debe imprimir cada línea en la consola. 
# Usa un bucle while para leer el archivo línea por línea con readline()

myfile = open("datos.txt", "r")
while True:
    line = myfile.readline()
    if line == "":
        break
    print(line)
myfile.close()

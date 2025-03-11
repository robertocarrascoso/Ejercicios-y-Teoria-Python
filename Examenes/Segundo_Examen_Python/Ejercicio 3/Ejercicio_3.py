# Escribe un programa que abra un archivo llamado reporte.txt, 
# lea todas sus líneas utilizando readlines() y cuente cuántas 
# líneas tiene el archivo. Finalmente, imprime el número total de líneas

file = open("reporte_ej3.txt", "r")

archivo_terminal = file.readlines()

print("".join(archivo_terminal))
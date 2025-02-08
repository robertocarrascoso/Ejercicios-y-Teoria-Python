#Escritura
mi_archivo = open("escritos.txt", "w")
mi_texto = "¡Primera línea!\n¡Segunda línea!\n¡Última en la fila!"
print(mi_texto)
mi_archivo.write(mi_texto)
mi_archivo.close()


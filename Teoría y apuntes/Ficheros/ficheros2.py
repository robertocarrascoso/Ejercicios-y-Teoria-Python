#Añadir texto
mi_archivo = open("escritos.txt", "a")
texto_agregado = "¡Línea añadida!\nEsto va a escritos.txt! \
que fue creado anteriormente.\n"
print(texto_agregado)
mi_archivo.write(texto_agregado)
mi_archivo.close()


# Roberto Carrascoso Jordán - 1ºCFGM SMR

lista_libros = ["Geromito Stilton" , "Muerte en el Nilo" , "IT" , "Harry Potter" ,  "Metro 2033", "Cementerio de animales"]
print("\n1 - Lista de libros iniciales: ", " | ".join(lista_libros))

# 2 - Añadimos un libro
lista_libros.insert(6, "Frankeistein")
print("2 - Añadimos un libro: ", " | ".join(lista_libros))

# 3 - Borramos el libro llamato "IT"
lista_libros.remove("IT")
print("3 - Borramos el libro llamato IT: ", " | ".join(lista_libros))

# 4 - Extraemos el libro llamado "Muerte en el Nilo"
lista_libros.pop(1)
print("4 - Extraemos el libro llamado Muerte en el Nilo: ", " | ".join(lista_libros))

# 5 - Mostramos la lista al reves
lista_libros.reverse()
print("5 - Mostramos la lista al reves: ", " | ".join(lista_libros))

# 6 - Mostramos la lista ordenadamente
lista_libros.sort()
print("6 - Mostramos la lista ordenadamente: ", " | ".join(lista_libros))

# 7 - Añadimos un libro llamado "El señor de los anillos"
lista_libros.append("El señor de los anillos")
print("7 - Añadimos un libro llamado El señor de los anillos: ", " | ".join(lista_libros))

# 8 - Añadimos un libro llamado "Los Juegos del Hambre"
lista_libros.append("Los Juegos del Hambre")
print("8 - Añadimos un libro llamado Los Juegos del Hambre: ", " | ".join(lista_libros))

# 8.1 - Volvemos a añadir el libro IT
lista_libros.append("IT")
print("8.1 - Volvemos a añadir el libro IT: ", " | ".join(lista_libros))

# 9 - Borramos los dos libros IT y Metro 2033
del lista_libros[1:3]
print("9 - Borramos los dos libros IT y Metro 2033: ", " | ".join(lista_libros))

# 10 - Realizamos un conteo
num_veces = lista_libros.count("Geronimo Stilton")
print("10 - Realizamos un conteo de Geronimo Stilton: ", num_veces)

# 11 - Borramos la lista
lista_libros.clear()
print("11 - Borramos la lista: ", " | ".join(lista_libros))

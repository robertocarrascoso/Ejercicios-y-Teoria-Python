
# Creamos una lista
my_list = ["coche", "moto", "bicicleta"]

# Insertar un valor en la lista
my_list.insert(3,"patinete")

# Eliminar un valor de la lista
my_list.remove("moto")

#  Extraer/Quitar una cosa del objeto basado en su posición
my_list.pop(0)

# Eliminar valores de un rango hasta otro
del my_list[1:3]

# Obtener la cantidad de elementos en la lista
cant = len(my_list)
print("Cantidad de elementos:", cant)

# Para mostrar la lista desde atrás
my_list.reverse()

# Para copiar una lista
my_list_copy = my_list.copy()

# Obtener el índice de un elemento
index = my_list.index("coche")

# Enumerar la lista
my_list.sort()

# Limpiar la lista
my_list.clear()
# Escribe una lista de tareas en un archivo.

# 1 - Agrega una tarea en el txt
# 2 - Leer y mostrar todas las tareas del txt
# 3 - Agregar otra tarea sin borrar las anteriores
print("\n Tareas:")

with open ("tareas.txt", "w") as file:
    file.write("Lavarme los dientes\n")
    file.write("Ordenar habitación")

file = open("tareas.txt", "r")
line1 = file.readline()
line2 = file.readline()
print("Linea1: ", line1)
print("Linea2: ", line2)
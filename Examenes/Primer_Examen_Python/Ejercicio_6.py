# Roberto Carrascoso Jordán

# Programa que aplique el if, elif y else.

# Declaramos la variable
colorfavorito = ""

# Solicitamos un color al usuario y lo guardamos en la variable
colorfavorito = input("¿Cuál es tu color favorito?: ")

# Creamos una condición para saber si es el color salmon e imprimimos un mensaje personalizado.
if colorfavorito == "salmon":
    print("La mayoría diría que el salmón es un pez, pero supongo que tambíen cuenta como un color.")

# Creamos una condición para saber si es el color rojo e imprimimos un mensaje personalizado.
elif colorfavorito == "rojo":
    print("El rojo luce bien en un coche deportivo.")

# Creamos una condición para saber si es el color amarillo e imprimimos un mensaje personalizado.
elif colorfavorito == "amarillo":
    print("amarillo también es bonito.")

# Si el usuario pone otro color diferente, le decimos que ese color tambien es mi color
else:
    print("El",colorfavorito, "también es mi color")
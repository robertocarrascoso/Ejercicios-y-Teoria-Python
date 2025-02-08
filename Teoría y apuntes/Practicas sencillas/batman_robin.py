# Declaramos variables
nombre = ""
msg_bienvenida = "Bienvenido a Gotham "
msg_batman = "Hola, Batman."
msg_robin = "Hola, Robin."

# Pedimos que nos diga su nombre
nombre = input(msg_bienvenida + "¿Cual es tu nombre?: ")

# Creamos la parte que se muestra en pantalla con el saludo.
if nombre.lower() == "Batman":
    print(msg_batman) # Escribimos el nombre que ha escrito

elif nombre.lower() == "Robin":
    print(msg_robin) # Escribimos el nombre que ha escrito

else:
    print(msg_bienvenida + nombre + ", no te conocíamos")
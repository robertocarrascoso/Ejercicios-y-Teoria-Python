
# Roberto Carrascoso Jordán - 1ºA CFGM SMR

# Ejercicio de revisión de restaurantes

# Declaramos las variables y su contenido
msg_incial = "Buenas! \nEsperemos que le haya gustado nuestro servicio.\n \nNos gustaria realizarle una encuesta de satisfacción:"
usr_calificacion = ""

# Iniciamos la interacción con el usuario
print(msg_incial)

# Pedimos la calificación
usr_calificacion = float(input("¿Del 1 al 10 como de satisfactoria ha sido tu experiencia?: "))

# Creamos las condiciones
if usr_calificacion > 10 or usr_calificacion < 1:
    print("Calificación no válida.")
elif usr_calificacion >= 9:
    print("Has calificado ⭐️⭐️⭐️⭐️⭐️, muchas gracias!")
elif usr_calificacion >= 7:
    print("Has calificado ⭐️⭐️⭐️⭐️, muchas gracias!")
elif usr_calificacion >= 5:
    print("Has calificado ⭐️⭐️⭐️, muchas gracias!")
elif usr_calificacion >= 3:
    print("Has calificado ⭐️⭐️, muchas gracias!")
elif usr_calificacion >= 1:
    print("Has calificado ⭐️, muchas gracias!")
else:
    print("Calificación no válida.")
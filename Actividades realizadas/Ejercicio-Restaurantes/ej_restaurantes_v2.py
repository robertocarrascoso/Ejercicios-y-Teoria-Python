
# Roberto Carrascoso Jordán - 1ºA CFGM SMR

# Ejercicio de revisión de restaurantes

# Declaramos las variables y su contenido
msg_incial = "Buenas! \nEsperemos que le haya gustado nuestro servicio.\n \nNos gustaria realizarle una encuesta de satisfacción:"
usr_calificacion = ""

# Iniciamos la interacción con el usuario
print(msg_incial)

# Pedimos la calificación
usr_calificacion = float(input("¿Del 1 al 5 como de satisfactoria ha sido tu experiencia?: "))

# Creamos las condiciones
if usr_calificacion > 5 or usr_calificacion < 1:
    print("Calificación no válida.")
elif usr_calificacion >= 5:
    print("¡Has calificado ⭐️⭐️⭐️⭐️⭐️! Eres increíble, gracias por tu apoyo incondicional.")
elif usr_calificacion >= 4:
    print("¡Has calificado ⭐️⭐️⭐️⭐️! Nos alegra mucho saber que te ha gustado, gracias por tu confianza.")
elif usr_calificacion >= 3:
    print("¡Has calificado ⭐️⭐️⭐️! Valoramos mucho tu valoración, gracias por elegirnos.")
elif usr_calificacion >= 2:
    print("¡Has calificado ⭐️⭐️! Gracias por darnos la oportunidad de mejorar.")
elif usr_calificacion >= 1:
    print("¡Has calificado ⭐️! Agradecemos tu cordialidad, trabajaremos para hacerlo mejor.")
else:
    print("Calificación no válida.")
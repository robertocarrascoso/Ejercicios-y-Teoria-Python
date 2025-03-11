# En una plataforma de comercio electrónico, los usuarios pueden calificar 
# productos con un sistema de 5 estrellas (⭐️⭐️⭐️⭐️⭐️). 
# La calificación puede incluir valores decimales (por ejemplo, 4.5 o 3.8) 
# y un comentario opcional sobre su experiencia con el producto. 

# Instrucciones => Únicamente usa input() para pedir la calificación y 
# conviértela en un número flotante (float). Usa if/elif/else para 
# clasificar la calificación en diferentes niveles de satisfacción


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
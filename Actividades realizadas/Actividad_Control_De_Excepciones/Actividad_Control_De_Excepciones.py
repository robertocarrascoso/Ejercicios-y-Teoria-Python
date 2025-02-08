enviar_mensaje = 'Oye tú! Esto es un mensaje secreto.'

with open('enviar_mensaje.txt', 'w') as file:
    file.write(enviar_mensaje)

with open('enviar_mensaje.txt', 'r+') as file:
    mensaje_original = file.read()
    file.seek(0)
    file.truncate(20)
    
    file.seek(0)
    mensaje_truncado = file.read()

print("Mensaje original:")
print(mensaje_original)
print("\nMensaje truncado:")
print(mensaje_truncado)
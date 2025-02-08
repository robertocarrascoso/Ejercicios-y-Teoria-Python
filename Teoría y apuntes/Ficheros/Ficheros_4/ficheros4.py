enviar_mensaje = 'Oye tú! esto es un mensaje secreto.'

with open('enviar_mensaje.txt', 'w') as file:
    file.write(enviar_mensaje)

with open('enviar_mensaje.txt', 'r+') as file:
    
    mensaje_orginial = file.read()
    
    file.seek(5)
    print(file.read())
    print("---\n")
    
    file.truncate(6) 
    print(file.read())
    
    unset_mensaje = 'Este mensaje no ha sido enviado.'

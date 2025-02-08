enviar_mensaje = 'Oye tú! Esto es un mensaje secreto.'

with open('enviar_mensaje.txt', 'w') as file:
  file.write(enviar_mensaje)
  
with open('enviar_mensaje.txt', 'r+') as file:
  
  mensaje_original = file.read()
      
  file.seek(0)
  
  unsent_mensaje = 'Este mensaje no ha sido enviado.'
  
  
# Programa que solicite nombre de usuario y contraseña, y de una bienvenida

# Declaramos las variables que vamos a utilizar
usr_dado = ""
pswd_dada = ""
usuario = ""
contraseña = ""

# Decimos de que va el progama
print("Vamos a crear tu usuario.")

# Solicitamos y guardamos el nombre de usuario
usr_dado = input("Nombre de usuario?: ")
pswd_dada = input("Contraseña para tu usuario?: ")

print("Usuario creado con éxito!")

# Vamos a solicitar el usuario
usuario = input("Introduce tu nombre de usuario: ")

# Verificamos si el usuario es el inicial
if usuario == usr_dado:
    # Si el usuario es correcto, solicitamos la contraseña
    contraseña = input("Introduce tu contraseña: ")
    # Comprobamos si la contraseña es correcta
    if contraseña == pswd_dada:
        print("Bienvenido ",usr_dado)
    else:
        print("La contraseña es incorrecta.")
else:
    print("El usuario no existe.")
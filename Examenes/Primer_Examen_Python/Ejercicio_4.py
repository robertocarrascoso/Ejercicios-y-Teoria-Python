# Roberto Carrascoso Jordán

# Programa que solicite nombre de usuario y contraseña

# Declaramos las variables que vamos a utilizar
usuario = ""
contraseña = ""

# Solicitamos y guardamos el nombre de usuario
usuario = input("Usuario?: ")

# Verificamos si el usuario es "Paco"
if usuario == "Paco":
    # Si el usuario es correcto, solicitamos la contraseña
    contraseña = input("Contraseña?: ")
    # Comprobamos si la contraseña es correcta
    if contraseña == "Salesianos123":
        print("Bienvenido Paco!")
    else:
        print("La contraseña es incorrecta.")
else:
    print("El usuario no es correcto.")
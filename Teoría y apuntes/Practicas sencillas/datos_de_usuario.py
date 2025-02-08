# Primero, declaramos las variables
nombre = ""
edad = ""
altura = ""
sexo = False  # Inicialmente, se asume Femenino
direccion = ""

# Solicitamos los datos al usuario

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
altura = input("Ingrese su altura en metros: ")
sexo_input = input("Ingrese su sexo (Masculino/Femenino): ")

# Como tenemos un booleano....tenemos que manejar esa información y 
# convertir la entrada a un valor booleano. Es decir true, será 
# másculino y false será femenino.

if sexo_input.lower() == "masculino":
    sexo = True  # Masculino es True
elif sexo_input.lower() == "femenino":
    sexo = False  # Femenino es False
else:
    print("Sexo no válido. Se asignará Femenino (False) por defecto.")
    
direccion = input("Ingrese su dirección: ")

# Mostrar los datos al usuario
print("\n--- Datos Indicados ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura} metros")
print(f"Sexo: {'Masculino' if sexo else 'Femenino'}")
print(f"Dirección: {direccion}")
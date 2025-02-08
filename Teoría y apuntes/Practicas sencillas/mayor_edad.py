# Declarar variables
edad = 0
resultado_menor = "Eres menor de edad."
resultado_mayor = "Eres mayor de edad."

# Pedimos su edad, y hacemos una excepción por si pone un valor erroneo.
try:
    edad = int(input("Buenas, introduzca su edad: "))

except ValueError:
    print("Por favor, introduce un número válido.")

# Comprobamos la edad y damos resultado

if edad < 18:
    print(resultado_menor)
else:
    print(resultado_mayor)
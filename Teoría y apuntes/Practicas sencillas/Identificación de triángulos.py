# SEGUNDO EJERCICIO: Identificación de triángulos

# Declaración de variables 
msg_equilatero = "Es un triángulo equilátero."
msg_isosceles = "Es un triángulo isósceles."
msg_escaleno = "Es un triángulo escaleno."

lado1 = 0
lado2 = 0
lado3 = 0

try:
    # Pedimos los datos al usuario
    lado1 = float(input("Ingrese la longitud del primer lado: "))
    lado2 = float(input("Ingrese la longitud del segundo lado: "))
    lado3 = float(input("Ingrese la longitud del tercer lado: "))

except ValueError:
    print("Ingrese un número válido.")


# Creamos la condición y resultados
if lado1 == lado2 == lado3:
    print(msg_equilatero)
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print(msg_isosceles)
else:
    print(msg_escaleno)
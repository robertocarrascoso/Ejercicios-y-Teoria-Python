# PRIMER EJERCICIO

# Declaramos variables
dato1 = 0
operador = ""
dato2 = 0
resultado = 0

# Pedimos los datos
try:

    dato1 = input("Ingrese el primer dato: ")
    operador = input("Escoja un operador: + , - , * , / : ")
    dato2 = input("Ahora ingrese el segundo dato: ")

except ValueError:
    print("Ingrese un valor válido.")

# Convertir los datos a números
dato1 = int(dato1)
dato2 = int(dato2)

# Condiciones para realizar el calculo y el calculo
if operador == "+" :
    resultado = dato1 + dato2
elif operador == "-":
    resultado = dato1 - dato2 
elif operador == "*":
    resultado = dato1 * dato2 
elif operador == "/":
    resultado = dato1 / dato2


# Mostrar el resultado
print("La suma de los dos datos es:", resultado)
# Estructura de datos con criterio de finalización II

# Declaramos variables
num_1 = 0
num_2 = 0
oper_usr = 0
resultado = 0

# Enseñamos al usuario las distintas operaciones
def operaciones():
    print("\nEscriba el número de una de estas operaciones: \n (1) Sumar \n (2) Restar \n (3) Multiplicar \n (4) Dividir \n (5) Cambiar los números actuales. \n (6) Salir del programa.")
    return int(input("Selecciona una opción: "))

# Pedimos los datos iniciales
num_1 = int(input("Introduzca el primer número: "))
num_2 = int(input("Introduzca el segundo número: "))

# Bucle principal
while True:
    oper_usr = operaciones()
    if oper_usr == 1:
        resultado = num_1 + num_2
        print(f"El resultado de la suma es:",resultado)
    
    elif oper_usr == 2:
        resultado = num_1 - num_2
        print(f"El resultado de la resta es:",resultado)
    
    elif oper_usr == 3:
        resultado = num_1 * num_2
        print(f"El resultado de la multiplicación es:",resultado)
    
    elif oper_usr == 4:
        if num_2 != 0:  # Evitar división por cero
            resultado = num_1 / num_2
            print(f"El resultado de la división es:",resultado)
        else:
            print("Error: No se puede dividir entre cero.")
    
    elif oper_usr == 5:
        num_1 = int(input("Introduzca el primer número: "))
        num_2 = int(input("Introduzca el segundo número: "))
    
    elif oper_usr == 6:
        print("Hasta otro momento.")
        break  # Sale del bucle y termina el programa
    else:
        print("Opción no válida, por favor seleccione una opción válida.")

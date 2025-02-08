# Programa Calculadora del radio.

try:
    # Declaramos variables

    pi = 3.141592
    radio = 0
    longitud = 0
    area = 0

    # Solicitamos el radio en milímetros
    radio = float(input("Introducir radio (en milímetros): "))

    # Realizamos los cálculos
    radio = radio / 1000
    longitud = 2 * pi * radio
    area = pi * radio * radio

    # Imprimimos las soluciones
    print("Área (en metros cuadrados): ", area)
    print("Longitud (en metros): ", longitud)
except ValueError:
    print("Introduzca un valor válido.")
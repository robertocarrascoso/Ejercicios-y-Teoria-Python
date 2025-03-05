
def mayor_de_edad(edad):
    if edad <= 18:
        print(f"Tienes {edad}. Eres menor de edad.")
    elif edad >= 18:
        print(f"Tienes {edad}. Eres mayor de edad.")
    else:
        print("Introduce un número válido.")

mayor_de_edad(15)

mayor_de_edad(26)
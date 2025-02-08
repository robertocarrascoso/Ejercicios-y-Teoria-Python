# Declarar variables
nota = 0
resultado_suspenso = "Vaya, has suspendido."
resultado_aprobado = "Has aprobado."
resultado_bien = "Has sacado un bien!"
resultado_notable = "Muy bien, has sacado un notable."
resultado_sobresaliente = "Enhorabuena, has sacado un sobresaliente."

# Pedir nota al usuario
try: 
    nota = float(input("Buenas, ¿qué nota has sacado?: "))

except ValueError:
    print("Por favor, introduce un número válido.")

# Comprobamos su nota y resultado
if nota <1 or nota > 10: 
    print("La nota debe de estar entre 1 y 10.")
else: 
    if nota < 5:
        print(resultado_suspenso)
    
    elif 5 <= nota < 6:
        print(resultado_aprobado)

    elif 6 <= nota < 7:
        print(resultado_bien)

    elif 7 <= nota < 9:
        print(resultado_notable)

    elif 9 <= nota <= 10:
        print(resultado_sobresaliente)
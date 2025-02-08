# Declarar variables
nota = 0
resultado_suspenso = "Has suspendido."
resultado_aprobado = "Has aprobado."
resultado_bien = "Has sacado un bien."
resultado_notable = "Has sacado un notable."
resultado_sobresaliente = "Has sacado un sobresaliente."

# Pedir nota al usuario
nota = float(input("Buenas, ¿qué nota has sacado?: "))

# Comprobamos su nota y resultado
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
def persona (nombre, edad, sexo):
    print("Soy", nombre+",", "tengo", edad, "años", "y soy" , sexo)

persona("Isma", 23, "un misil tomahok")

def añadir(x, y):
    respuesta = x + y
    return respuesta

x = int(input("Dame un número: "))
y = int(input("Dame otro número: "))

resultado = añadir(x, y)
print("El resultado de la suma es:", resultado)

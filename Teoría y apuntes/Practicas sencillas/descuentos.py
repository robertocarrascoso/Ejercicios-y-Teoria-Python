# Declaramos la variable
edad = 0

# Leemos la variable edad y hacemos una condición para no coger datos erroneos
try:
    edad = int(input("Buenas, introduzca su edad: "))

except ValueError:
    print("Por favor, introduce un número válido.")

# Hacemos la condición par dar el descuento
if edad <12: 
    print("Descuento del 50%")
elif edad <= 18:
    print("Descuento del 20%")
else:
    print("Sin descuento") 
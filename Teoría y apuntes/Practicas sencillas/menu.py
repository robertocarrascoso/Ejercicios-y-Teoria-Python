saludo = "Bienvenido a Pico Rico!"
pedido = ""
opc1 = "Hamburguesa con papas fritas"
opc2 = "Pizza con una pepsi"
op3 = "Ensalada con agua"
opc4 = "Salir del restaurante"

# Saludamos al cliente
print(saludo)

# Preguntamos que quiere pedir
pedido = input("Que deseas pedir? \n1.-" + opc1 + "\n2.-" + opc2 + "\n3.-" + op3 + "\n4.-" + opc4 + "\n")

if pedido == opc1:
    print("Son 12€, por favor.")
    
elif pedido == opc2:
    print("Son 8.50€, por favor.")
elif pedido == op3:
    print("Son 4.23€, por favor.")
elif pedido == opc4:
    print("Gracias por su visita.")
else:
    print("No tenemos esa opción en el menú.")

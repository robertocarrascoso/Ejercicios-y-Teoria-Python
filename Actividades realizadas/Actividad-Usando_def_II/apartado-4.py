# 4. Crea una función calcular_precio_con_descuento(precio, descuento) que reciba un precio y un porcentaje de descuento, y devuelva el precio final después del descuento.

def calcular_precio_con_descuento(precio, descuento):
    precio_final = precio - (precio * descuento * 0.01)
    print(precio_final)

calcular_precio_con_descuento(20, 20)

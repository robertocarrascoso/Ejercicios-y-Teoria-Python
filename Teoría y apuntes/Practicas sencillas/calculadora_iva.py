# Calculadora de IVA en una factura

# Declaramos variables
IVA = 0.16
base_imponible = 0.0
total_factura = 0.0

# Pedimos la información
base_imponible = float(input("Introduzca la base imponible: "))

# Hacemos el cálculo
total_factura = (base_imponible + base_imponible * IVA)

# Imprimimos el resultado
print("Total de la factura: ", total_factura)

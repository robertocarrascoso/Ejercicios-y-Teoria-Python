for a in range(9):
    if a == 3:
        continue
    print(a)

##########################################

i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    print(i)

##########################################

for i in range(9):
    if i > 10:
        break
    print(i)

##########################################

coches = ["toyota", "ford", "Hyundai"]
miCoche = len(coches)
print(miCoche)

miCoche2 = coches [2]
print(miCoche2)

##########################################

def mi_funcion():
    print("hola mundo")

mi_funcion()

##########################################

def mi_funcion(primerNombre):
    print("El mejor nombre es: ", 
        primerNombre[2])

mi_funcion("Aitor", "Juan", "Elvis")

##########################################

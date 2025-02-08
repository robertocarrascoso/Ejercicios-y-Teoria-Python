## Ejemplo de range 
for i in range(5):
    print(i)

## Ejemplo de range 
for i in range(104, 109):
    print(i)

## Ejemplo de range 
number = 3
for i in range(number):
    print(i)

## Creación de una colección.
frutas = ["tamaringo", "naranja", "uvas", "mango"]
for i in frutas:
    print(i)

## Acceder a la colección
frustas = ["tamaringo", "naranja", "uvas", "mango"]
print(frutas[2])

## Creaciób de listas

nueva_fruta  = list(frutas)
nueva_fruta [1] = "piña"
frutas = tuple(nueva_fruta)

print(frutas)

## Creación lista
frutas = {"tamaringo", "naranja", "uvas", "mango"}
frutas.remove("naranja")
print(frutas)

#Escribir en texto
with open ("1AGM.txt", "w") as file:
    file.write("hola 1AGM\n")
    file.write("hola otra vez 1AGM\n")
    file.write("hola por 3 1AGM\n")



#print("esto es para 1AGM")

#Leer en texto

#file = open("1AGM.TXT", "r")
#contenido = file.read()
#linea1= file.readline()
#print(linea1, end="")

#Para que lea la primera linea

#file = open("1AGM.TXT", "r")
#linea1= file.readline()
#print(linea1, end="")
#print("Primera linea:", linea1)



file = open("1AGM.TXT", "r")
linea = file.readlines()
for linea in linea:
    print(linea, end='')
















# New commands to try and then close the program.

try:
    file = open("archivo.txt", "r") # We try to open the "archivo.txt", and if we can, we readit.

finally:
    file.close() # Finally, we close the script.

###

with open('example.txt', 'r') as file:
    file.seek(10) # Imprimir a partir del caracter 10 
    content = file.read()

###

with open('example.txt', 'a') as file:
    file.truncate(20) # Truncate the file to 20 characters
    content_2 = file.read()
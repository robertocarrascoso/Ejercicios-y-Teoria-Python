with open("example.txt", "r") as file:
    file.seek(10) # Imprimir a partir del caracter 10 
    content = file.read()
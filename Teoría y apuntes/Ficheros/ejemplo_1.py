with open("example.txt", "a") as file:
    file.truncate(20) # Imprimir hasta el caracter 20
    content_2 = file.read('example.txt')
    
    print(content_2)
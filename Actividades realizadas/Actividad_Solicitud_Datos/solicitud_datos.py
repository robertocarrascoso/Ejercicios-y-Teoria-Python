
# Roberto Carrascoso Jordán - 1ºA CFGM SMR

# Fundamentos de la programación - 04/02/2025

file_name = (input("Proporciona un nombre al doc sin extensión: ") + ".txt")
file_text =  input("Escribe algo: ")

with open(file_name, "w") as file:
    file.write("Usuario escribió: " + file_text)

print("\nResultado final:")
print("El nombre proporcionado para el doc fue: " + file_name)
print("El usuario escribió: " + file_text)
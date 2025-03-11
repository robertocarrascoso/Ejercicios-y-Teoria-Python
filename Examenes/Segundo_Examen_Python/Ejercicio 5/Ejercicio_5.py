# Crea un programa que pregunte al usuario 
# "¿Cuál es tu animal favorito?" y responda de manera 
# personalizada usando if, elif y else

user_animal_fav = ""

user_animal_fav = input("Escribe el nombre de tu animal favorito: ")

if user_animal_fav == "tigre":
    print("El", user_animal_fav, "es un cazador sigiloso y poderoso")
elif user_animal_fav == "perro":
    print("El", user_animal_fav, "es el mejor animal de compañia.")
elif user_animal_fav == "gato":
    print("El", user_animal_fav, "en ocasiones es sigiloso, en otras, cariñoso.")
elif user_animal_fav == "tlacuache":
    print("El", user_animal_fav, "también es el animal favortio de Geremy.")
elif user_animal_fav == "cabra":
    print("La", user_animal_fav, "es el animal que mejor representa a Fernando Alonso.")
elif user_animal_fav == "nutria":
    print("La", user_animal_fav, "es un animal un tanto extraño.")
else:
    print("El", user_animal_fav, "es un animal precioso.")
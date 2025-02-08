file_path = "example.txt"

try:
    file = open(file_path, "r") # We try to open the "archivo.txt", and if we can, we readit.
finally:
    file.close() # Finally, we close the script.
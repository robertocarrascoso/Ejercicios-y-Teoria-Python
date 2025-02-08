try:
  file = open('ejemplo.txt', 'r')
 
finally:
  file.close()
  
  
#####################################################


file_path = 'example.txt'

try:
  file = open(file_path, 'r')
 
finally:
  file.close()

with open('example.txt', 'r') as file:
  content = file.read()
  print(content)


######################################################



with open('example.txt', 'r') as file:
  file.seek(10)  
  content = file.read()
  
  
  
#####################################################


with open('example.txt', 'a') as file:
  file.truncate(20)

  

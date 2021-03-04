import random

max_number = 10000000
random_limit = 999999
filename = "generatedfiles/"+str(max_number)+".txt"

file = open(filename, "w")
for i in range(max_number):
    file.write(str(random.randint(1,random_limit)))
    if i!=(max_number-1): # Проверка последнее ли это число, чтобы ставить пробел
        file.write(' ')
file.close()
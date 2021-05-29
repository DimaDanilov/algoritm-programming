import time

arr_num = 1000 # Выбор файла
filename = "generatedfiles/" + str(arr_num) + ".txt"

# Считывание массива из файла
file = open(filename, "r")
arr = (file.read()).split(' ') # Считывание строки и разбиение её на массив
for i in range(len(arr)): 
    arr[i] = int(arr[i]) # Перевод массива строк в массив чисел


def insertionsort(array):
    for i in range(1, len(array)):
        insert_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > insert_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = insert_item


start_time = time.time()
insertionsort(arr)
print("--- %s seconds ---" % (time.time() - start_time))



# Запись в файл
filename = "sortedfiles/insertion_"+str(arr_num)+".txt"
file = open(filename, "w")
for i in range(len(arr)):
    file.write(str(arr[i]))
    if i!=(len(arr)-1): # Проверка последнее ли это число, чтобы ставить пробел
        file.write(' ')
file.close()
arr_num = 10 # Выбор файла
filename = "generatedfiles/" + str(arr_num) + ".txt"

# Считывание массива из файла
file = open(filename, "r")
arr = (file.read()).split(' ') # Считывание строки и разбиение её на массив
for i in range(len(arr)): 
    arr[i] = int(arr[i]) # Перевод массива строк в массив чисел


# Тип сортировки
# bubble - пузырьком
# insertion - вставками
# selection - выборкой
sorttype = 'selection'

if sorttype == 'bubble':
    # Сортировка пузырьком
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
elif sorttype == 'insertion':
    # Сортировка вставками
    for i in range(1, len(arr)):
        insert_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > insert_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = insert_item
elif sorttype == 'selection':
    # Сортировка выборкой
    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]


# Запись в файл
filename = "sortedfiles/"+sorttype+"_"+str(arr_num)+".txt"
file = open(filename, "w")
for i in range(len(arr)):
    file.write(str(arr[i]))
    if i!=(len(arr)-1): # Проверка последнее ли это число, чтобы ставить пробел
        file.write(' ')
file.close()
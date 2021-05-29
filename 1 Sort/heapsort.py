import time

arr_num = 1000 # Выбор файла
filename = "generatedfiles/" + str(arr_num) + ".txt"

# Считывание массива из файла
file = open(filename, "r")
arr = (file.read()).split(' ') # Считывание строки и разбиение её на массив
for i in range(len(arr)): 
    arr[i] = int(arr[i]) # Перевод массива строк в массив чисел


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)
 
def heapSort(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)



start_time = time.time()
heapSort(arr)
print("--- %s seconds ---" % (time.time() - start_time))


# Запись в файл
filename = "sortedfiles/heapsort_"+str(arr_num)+".txt"
file = open(filename, "w")
for i in range(len(arr)):
    file.write(str(arr[i]))
    if i!=(len(arr)-1): # Проверка последнее ли это число, чтобы ставить пробел
        file.write(' ')
file.close()
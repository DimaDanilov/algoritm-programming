import random
import time

arr_num = 10000000 # Выбор файла
filename = "generatedfiles/" + str(arr_num) + ".txt"

# Считывание массива из файла
file = open(filename, "r")
arr = (file.read()).split(' ') # Считывание строки и разбиение её на массив
for i in range(len(arr)): 
    arr[i] = int(arr[i]) # Перевод массива строк в массив чисел

def bubblesort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

def insertionsort(array):
    for i in range(1, len(array)):
        insert_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > insert_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = insert_item

def selectionsort(array):
    for i in range(len(array)):
        minIndex = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]

def quicksort(array):
    # print('nums =', nums)
    if len(array) <= 1:
        return array
    else:
        c = random.choice(array)
        el_smaller = []
        el_larger = []
        el_equal = []
        for i in array:
            if i < c:
                el_smaller.append(i)
            elif i > c:
                el_larger.append(i)
            else:
                el_equal.append(i)
        answer = quicksort(el_smaller) + el_equal + quicksort(el_larger)
        return answer

def mergeSort(arr):
    if len(arr) > 1:
 
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
 
        mergeSort(left)
        mergeSort(right)
 
        i = 0
        j = 0
        k = 0
 
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
 

# Тип сортировки
# bubble - пузырьком
# insertion - вставками
# selection - выборкой
# qsort - быстрая
# merge - слиянием
sorttype = 'merge'

if sorttype == 'bubble':
    start_time = time.time()
    bubblesort(arr)
    print("--- %s seconds ---" % (time.time() - start_time))
elif sorttype == 'insertion':
    start_time = time.time()
    insertionsort(arr)
    print("--- %s seconds ---" % (time.time() - start_time))
elif sorttype == 'selection':
    start_time = time.time()
    selectionsort(arr)
    print("--- %s seconds ---" % (time.time() - start_time))
elif sorttype == 'qsort':
    start_time = time.time()
    quicksort(arr)
    print("--- %s seconds ---" % (time.time() - start_time))
    arr = quicksort(arr)
elif sorttype == 'merge':
    start_time = time.time()
    mergeSort(arr)
    print("--- %s seconds ---" % (time.time() - start_time))


# Запись в файл
filename = "sortedfiles/"+sorttype+"_"+str(arr_num)+".txt"
file = open(filename, "w")
for i in range(len(arr)):
    file.write(str(arr[i]))
    if i!=(len(arr)-1): # Проверка последнее ли это число, чтобы ставить пробел
        file.write(' ')
file.close()
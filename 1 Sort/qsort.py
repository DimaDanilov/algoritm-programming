import random
import time

arr_num = 1000 # Выбор файла
filename = "generatedfiles/" + str(arr_num) + ".txt"

# Считывание массива из файла
file = open(filename, "r")
arr = (file.read()).split(' ') # Считывание строки и разбиение её на массив
for i in range(len(arr)): 
    arr[i] = int(arr[i]) # Перевод массива строк в массив чисел


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


start_time = time.time()
quicksort(arr)
print("--- %s seconds ---" % (time.time() - start_time))
arr = quicksort(arr)


filename = "sortedfiles/qsort_"+str(arr_num)+".txt"
file = open(filename, "w")
for i in range(len(arr)):
    file.write(str(arr[i]))
    if i!=(len(arr)-1): # Проверка последнее ли это число, чтобы ставить пробел
        file.write(' ')
file.close()
import random

filename = "input.txt"

# Считывание массива из файла
file = open(filename, "r")
input_arr = (file.read()).split(' ') # Считывание строки и разбиение её на массив
file.close()

# Инициализация переменных
Q = int(input_arr[0])
V = int(input_arr[1])
P = int(input_arr[2])
N = int(input_arr[3])
K = int(input_arr[4])
arr = [P]

# Быстрая сортировка
def quicksort(array):
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

# Рассчет значений массива
for i in range(1, N):
    arr.append((arr[i-1] * Q) % V)
arr = quicksort(arr)


# Вывод в консоль
# for i in range (len(arr)):
#     print ('arr[' + str(i+1) + '] = ' + str(arr[i]))


# Запись в файл
filename = "output.txt"
file = open(filename, "w")
file.write(str(arr[K-1]))
file.close()
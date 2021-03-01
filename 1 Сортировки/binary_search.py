arr_num = 10 # Выбор файла
filename = "sortedfiles/bubble_" + str(arr_num) + ".txt"

# Считывание массива из файла
file = open(filename, "r")
arr = (file.read()).split(' ') # Считывание строки и разбиение её на массив
for i in range(len(arr)): 
    arr[i] = int(arr[i]) # Перевод массива строк в массив чисел
print(arr)

value = int(input("Введите элемент ID которого вы ищите = "))

mid = len(arr) // 2
low = 0
high = len(arr) - 1

while arr[mid] != value and low <= high:
    if value > arr[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("Элемент не найден")
else:
    print("ID =", mid)
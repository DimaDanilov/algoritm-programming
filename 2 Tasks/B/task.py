filename = "input.txt"

# Считывание массива из файла
file = open(filename, "r")
arr = file.read().split() # Считывание строки и разбиение её на массив
file.close()

# Перевод массива строк в массив чисел
for i in range(len(arr)): 
    arr[i] = int(arr[i])

N = int(arr[0])
del arr[0]
C = 0

for i in range(0, N-1):
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            C+=1

# Вывод в консоль
# print ("N = "+str(N))
# print ("C = "+str(C))
# for i in range (len(arr)):
#     print ('arr[' + str(i+1) + '] = ' + str(arr[i]))

filename = "output.txt"
file = open(filename, "w")
file.write(str(C))
file.close()
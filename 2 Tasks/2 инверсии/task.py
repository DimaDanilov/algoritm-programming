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
        global C
 
        while ((i < len(left)) and (j < len(right))):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                C += (len(left)-i)
                # print(C, left[i], right[j])
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


mergeSort(arr)
# Вывод в консоль
# print ("N = "+str(N))
# print ("C = "+str(C))
# for i in range (len(arr)):
#     print ('arr[' + str(i+1) + '] = ' + str(arr[i]))

filename = "output.txt"
file = open(filename, "w")
file.write(str(C))
file.close()
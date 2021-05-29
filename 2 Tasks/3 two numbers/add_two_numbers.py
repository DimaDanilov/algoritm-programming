# Инициализация переменных
arr1 = [2,4,3]
arr2 = [5,6,4]



# Функции

# На вход получает массив чисел. На выходе получается тоже массив чисел, но задом наперёд.
def Reverse(arr):
    # Делим массив на 2 части, и меняем местами эл-ты с начала первой половины и конца второй (1 и 9, 2 и 8, и т.д.)
    arr_len = len(arr)
    mid = arr_len/2
    i=1
    while (i<=mid):
        temp = arr[i-1]
        arr[i-1]=arr[arr_len-i]
        arr[arr_len-i]=temp
        i = i+1
    return arr


# Превращает массив чисел в одно слитое число. На входе массив чисел. На выходе одно число.
def ToNumber(arr):
    num1 = ''
    for i in range(len(arr)):
        num1=num1+str(arr[i])
    return int(num1)


# Сумма двух чисел
def Sum(a, b):
    return a+b


# Разбивает число на массив чисел. На входе число, на выходи массив чисел
def ToArray(num):
    array = list(str(num))
    # Перевод эл-тов в числа числа
    for i in range (len(array)):
        array[i] = int(array[i])
    return array




# Код

# Массивы чисел задом наперёд
arr1 = Reverse(arr1)
arr2 = Reverse(arr2)


# Числа полученные от слияния массива в одно число
num1 = ToNumber(arr1)
num2 = ToNumber(arr2)


# Сумма 2-х чисел
num3 = Sum(num1, num2)


# Разбиение числа на массив чисел
arr3 = ToArray(num3)


# Запись массива задом наперёд
answer = Reverse(arr3)



# Вывод в консоль
# print(num1,num2)
# print(num3)
# print(answer)
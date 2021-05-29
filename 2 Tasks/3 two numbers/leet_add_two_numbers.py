# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        arr1 = self.traverseToArr(l1)
        arr2 = self.traverseToArr(l2)
        # Код


    # Массивы чисел задом наперёд
        arr1 = self.Reverse(arr1)
        arr2 = self.Reverse(arr2)


        # Числа полученные от слияния массива в одно число
        num1 = self.ToNumber(arr1)
        num2 = self.ToNumber(arr2)


        # Сумма 2-х чисел
        num3 = self.Sum(num1, num2)


        # Разбиение числа на массив чисел
        arr3 = self.ToArray(num3)

        return self.ToListNode(arr3)
        
        
    def traverseToArr(self, llist: ListNode):
        no = []
        next = llist.next
        no.append(llist.val)
        unit = 10

        while next is not None:
            no.append(next.val)
            unit = unit * 10
            next = next.next

        return no



        # Функции

        # На вход получает массив чисел. На выходе получается тоже массив чисел, но задом наперёд.
    def Reverse(self, arr):
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
    def ToNumber(self, arr):
        num1 = ''
        for i in range(len(arr)):
            num1=num1+str(arr[i])
        return int(num1)


    # Сумма двух чисел
    def Sum(self, a, b):
        return a+b


    # Разбивает число на массив чисел. На входе число, на выходи массив чисел
    def ToArray(self, num):
        array = list(str(num))
        # Перевод эл-тов в числа числа
        for i in range (len(array)):
            array[i] = int(array[i])
        return array


    # Переводит массив в ListNode
    def ToListNode(self, arr):
        head = None
        for x in arr:
            head = ListNode(x, next=head)
        return head



    # Вывод в консоль
    # print(num1,num2)
    # print(num3)
    # print(answer)
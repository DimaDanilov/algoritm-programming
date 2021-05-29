class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        import random

        # Считывание массива из файла
        arr = nums # Считывание строки и разбиение её на массив
        for i in range(len(arr)): 
            arr[i] = int(arr[i]) # Перевод массива строк в массив чисел


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



        mergeSort(arr)

        return arr
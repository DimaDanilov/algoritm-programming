class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        import random

        # Считывание массива из файла
        arr = nums # Считывание строки и разбиение её на массив
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


        arr = quicksort(arr)

        return arr
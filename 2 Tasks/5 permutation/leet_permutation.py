class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Проходит по маленькому массиву и свапает местами 2 элемента
        def Swap(array, value, pos):
            for i in range(pos+1, len(array)):
                if array[i]<=value:
                    temp=array[pos]
                    array[pos]=array[i-1]
                    array[i-1]=temp
                    return array
            # Если пройдя по массиву варианта не нашел(нужно свапнуть нужный элемент с последним)
            temp=array[pos]
            array[pos]=array[len(array)-1]
            array[len(array)-1]=temp
            return array


        # Ф-ция записи нужной части массива задом наперёд
        # Делим часть массива на 2 части, и меняем местами эл-ты. Например надо сортировать 2-6 эл-ты. Меняем 2 и 6, 3 и 5
        def Reverse(array, pos):
            arr_len = len(array)-pos
            last = arr_len+pos
            mid = (arr_len/2)+pos
            i=pos
            while (i<mid):
                temp = array[i]
                array[i]=array[last-(i-pos)-1]
                array[last-(i-pos)-1]=temp
                i = i+1
            return array


        # Основная ф-ция. Если функция нуждается в проверке(длина>1), то проходит с конца массива до начала и выполняет 2 ф-ции
        def Permutation(arr):
            if (len(arr)>1):
                for i in range(len(arr)-2, -1, -1):
                    if arr[i]<arr[i+1]:
                        swapped = Swap(arr, arr[i], i)
                        reversed = Reverse(swapped, i+1)
                        return reversed
                # Если список оказался отсортированным по убыванию, необходимо отсортировать его по возрастанию
                return Reverse(arr, 0)

            # Если список состоит из 0-1 элементов
            else:
                return arr
        
        # Код
        nums = Permutation(nums)
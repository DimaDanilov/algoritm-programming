nums = [1,2,3]
arr = [[]]

for i in range(len(nums)):
    for j in range(len(arr)):
        temp = arr[j].copy()
        temp.append(nums[i])
        arr.append(temp)

print(arr)
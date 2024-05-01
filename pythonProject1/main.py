nums = [1,2,3,4,5,6,6]
n = len(nums)
for i in range(n - 1):
    for j in range(i + 1, n):
        print('i =', i , 'j = ' , j)
        if nums[i] == nums[j]:
            print('True')

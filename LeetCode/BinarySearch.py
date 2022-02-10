def search(nums, target):
    l = 0
    h = len(nums) -1
    while (h >= l):
        m = (l + h)//2
        if(nums[m] == target):
            return m
        if(nums[m] > target):
            h = m - 1
        if(nums[m] < target):
            l = m + 1
    return -1
print(search([1,2,3],3))
x = 1

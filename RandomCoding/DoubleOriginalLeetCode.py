def findFinalValue(nums, original):
    resp = original
    i = 0
    print(nums)
    nums = nums.sort()
    print(nums)
    restart = False
    while(i < len(nums)):
        restart = False
        while(i < len(nums) and restart == False):
            print(resp)
            if(nums[i] == resp):
                resp *= 2
                restart = True
            i += 1
    return reps

nums = [8,19,4,2,15,3]

original = 2
print(findFinalValue(nums, original))

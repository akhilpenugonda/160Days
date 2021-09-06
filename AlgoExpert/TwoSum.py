def twoNumberSum(array, targetSum):
    dictionary = {}
    for i in (array):
        num = targetSum - i
        if num in dictionary:
            return [num, i]
        else:
            dictionary[i] = num
    return []
print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
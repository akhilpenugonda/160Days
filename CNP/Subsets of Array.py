## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
arr = [int(ele) for ele in input().split()]


def ReturnSubsetsArray(nums):
    n = len(nums)
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]
    for a in output:
        for ele in a:
            print(ele, end = " ")
        print()
    return output
    
ReturnSubsetsArray(arr)
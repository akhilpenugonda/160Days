#FIniding umber of steps to reach stairs
def COuntSteps(n, arr):
    steps = [0]*(n+1)
    steps[0] = 1 
    steps[1] = 1
    for i in range(2, n+1):
        total = 0
        for j in arr:
            steps[i] = steps[i-1] + steps[i-2]
    return steps[n]
print(COuntSteps(5, [1,2]))
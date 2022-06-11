from sys import stdin
from sys import maxsize as MAX_VALUE
from sys import setrecursionlimit
setrecursionlimit(10**6)

dp = {}

def getMinSteps(n, memo):
    if(n == 1):
        return 0
    if(memo[n] != -1):
        return memo[n]
    res = getMinSteps(n-1, memo)
    if(n%2 == 0):
        res = min(res, getMinSteps(n//2, memo))
    if(n%3 == 0):
        res = min(res, getMinSteps(n//3, memo))
    memo[n] = 1 + res
    return memo[n]

def countMinStepsToOne(n):
    memo = [0 for i in range(n+1)]
    for i in range(n+1):
        memo[i] = -1
    return getMinSteps(n, memo)
#main
n = int(stdin.readline().rstrip())
print(countMinStepsToOne(n))
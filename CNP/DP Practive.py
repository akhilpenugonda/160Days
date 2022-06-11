import math, sys
def minSquares(n):
    if n == 0:
        return 0
    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1, root+1):
        currAns = 1 + minSquares(n - i**2)
        ans = min(ans, currAns)
    return ans

n = int(input())
ans = minSquares(n)
print(ans)

#Same using DP

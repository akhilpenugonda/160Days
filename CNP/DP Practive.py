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

def minSquaresMemo(n, dp):
    if n == 0:
        return 0
    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1, root+1):
        checkValue = n-i**2
        if(dp[checkValue] == -1):
            currAns = 1 + minSquaresMemo(n - i**2, dp)
            dp[checkValue] = currAns
        else:
            currAns = dp[checkValue]
        ans = min(ans, currAns)
    return ans



def minSquaresIter(n):
    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    for i in range(1, n+1):
        ans = sys.maxsize
        root = int(math.sqrt(i))
        for j in range(1, root+1):
            currAns = 1 + dp[i - j**2]
            ans = min(ans, currAns)
        dp[i] = ans
    return dp[n]


n = int(input())
dp = [-1 for i in range(n+1)]
ans = minSquares(n)
print(ans)
ans = minSquaresMemo(n, dp)
print(ans)
ans = minSquaresIter(n)
print(ans)

#Same using DP

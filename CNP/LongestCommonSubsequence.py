
from sys import stdin

def lcs(s, t, i, j) :
    if(i == len(s) or j == len(t)):
        return 0
    if(s[i] == t[j]):
        ans = 1 + lcs(s, t, i+1, j+1)
    else:
        ans1 = lcs(s, t, i+1, j)
        ans2 = lcs(s, t, i, j+1)
        ans = max(ans1, ans2)
        
    return ans

def lcsIter(s, t, i, j):
    n = len(s)
    m = len(t)
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if(s[i] == t[j]):
                dp[i][j] = 1+ dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    return dp[0][0]
def lcsDp(s, t, i, j, dp) :
    if(i == len(s) or j == len(t)):
        return 0
    if(s[i] == t[j]):
        if(dp[i+1][j+1] == -1):
            smallAns = lcsDp(s, t, i+1, j+1, dp)
            dp[i+1][j+1] = smallAns
            ans = 1 + smallAns
        else:
            ans = dp[i+1][j+1]
    else:
        if(dp[i+1][j] ==-1):
            ans1 = lcsDp(s, t, i+1, j, dp)
            dp[i+1][j]  = ans1
        else:
            ans1 = dp[i+1][j]
        if(dp[i][j+1] == -1):
            ans2 = lcsDp(s, t, i, j+1, dp)
            dp[i][j+1] = ans2
        else:
            ans2 = dp[i][j+1]
        ans = max(ans1, ans2)
        
    return ans
#main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())
dp = [[-1 for j in range(len(t)+1)] for i in range(len(s)+1)]
print(lcs(s, t, 0, 0))
print(lcsDp(s, t, 0, 0, dp))
print(lcsIter(s, t, 0, 0))
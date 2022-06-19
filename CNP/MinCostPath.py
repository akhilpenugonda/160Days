
from sys import stdin
MAX_VALUE = 2147483647

def minCostPath(cost, i, j, mRows, nCols, dp):
    if(i == mRows-1 and j == nCols-1):
        return cost[i][j]
    if(i >= mRows or j >= nCols):
        return MAX_VALUE
    if(dp[i][j+1] == MAX_VALUE):
        ans1 = minCostPath(cost, i, j+1, mRows, nCols, dp)
        dp[i][j+1] = ans1
    else:
        ans1 = dp[i][j+1]
    if(dp[i+1][j] == MAX_VALUE):
        ans2 = minCostPath(cost, i+1, j, mRows, nCols, dp)
        dp[i+1][j] = ans2
    else:
        ans2 = dp[i+1][j]
    if(dp[i+1][j+1] == MAX_VALUE):
        ans3 = minCostPath(cost, i+1, j+1, mRows, nCols, dp)
        dp[i+1][j+1] = ans3
    else:
        ans3 = dp[i+1][j+1]
        
    dp[i][j] = cost[i][j] + min(ans1, ans2, ans3)
    return dp[i][j]


#taking input using fast I/O method
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    mRows = int(li[0])
    nCols = int(li[1])
    
    if mRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(mRows)]
    return mat, mRows, nCols


#main
mat, mRows, nCols = take2DInput()
dp = [[MAX_VALUE for j in range(nCols+1)] for i in range(mRows+1)]
print(minCostPath(mat, 0, 0, mRows, nCols, dp))
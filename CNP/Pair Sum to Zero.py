from sys import stdin
from math import factorial
def nc2(n):
    ans = 0
    if(n != 1):
        ans = factorial(n)/(factorial(n-2)* 2)
    return ans

def pairSum0(l,n):
    dict = {}
    pairCount = 0
    for i in l:
        dict[i] = dict.get(i,0) + 1
    for k,v in dict.items():
        if(k > 0 and -k in dict):
            pairCount += v*dict[-k]
        if(k == 0):
            pairCount += nc2(dict[k])
        
    return int(pairCount)
        
def takeInput():
    #To take fast I/O
    n=int(stdin.readline().strip())
    if n==0:
        return list(),0
    arr=list(map(int,stdin.readline().strip().split( )))
    return arr,n

arr,n=takeInput()
print(pairSum0(arr,n))

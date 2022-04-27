from prometheus_client import Summary


def subsetSum(l):
    n = len(l)
    if n == 1:
        if l[0] == 0:
            return 1
        
    SumArray = [0]*len(l)
    SumArray[0] = l[0]
    dic = {}
    dic[l[0]] = 0
    start = 0
    mx = -1
    end = -1
    for i in range(1, n):
        SumArray[i] = l[i] + SumArray[i-1]
        if SumArray[i] == 0:
            mx = i + 1
            continue
        if SumArray[i] in dic:
            if mx == -1:
                start = dic[SumArray[i]]
                end = i
                mx = end - start
            elif i - dic[SumArray[i]] > mx:
                start = dic[SumArray[i]]
                end = i
                mx = i - dic[SumArray[i]]
        else:
            dic[SumArray[i]] = i
    return mx
            
# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))
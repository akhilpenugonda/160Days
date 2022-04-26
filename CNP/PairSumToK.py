def printPairDiffK(l, k):
    dict = {}
    totalPairs = 0
    for i in l:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for key,value in dict.items():
        if(k == 0):
            if(value > 1):
                totalPairs += (value * (value - 1))//2
            continue
        if((key-k) in dict):
            totalPairs += value * dict[key-k]
    return totalPairs
        
    
# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
print(printPairDiffK(l, k))
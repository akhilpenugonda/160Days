from sys import stdin
def findUniqueMergeSort(arr, n) :
    #print(arr)
    MergeSort(arr)
    #print(arr)
    i = 0
    while(i < len(arr)):
        if((i + 1) == len(arr)):
           return arr[i]
        if(arr[i] == arr[i+1]):
            i += 2
        else:
            return arr[i]
    return -1
def findUnique(arr, n) :
    #Using Xor
    r = 0
    i = 0
    while(i < len(arr)):
        r ^= arr[i]
        i+=1
    return r
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()
def Merge(a1,a2,a):
    i = 0
    j = 0
    k = 0
    while(i < len(a1) and j < len(a2)):
        if(a1[i] < a2[j]):
            a[k] = a1[i]
            i+=1
            k+=1
        else:
            a[k] = a2[j]
            j+=1
            k+=1
    while(i<len(a1)):
        a[k] = a1[i]
        k+=1
        i+=1
    while(j<len(a2)):
        a[k] = a2[j]
        j+=1
        k+=1
def MergeSort(a):
    if(len(a) == 1 or len(a) == 0):
        return
    m = len(a)//2
    a1 = a[0:m]
    a2 = a[m:]
    MergeSort(a1)
    MergeSort(a2)
    Merge(a1, a2, a)
        
#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(findUnique(arr, n))

    t-= 1
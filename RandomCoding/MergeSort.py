def mergeSort(a):
    if(len(a) == 1 or len(a) == 0):
        return
    m = len(a)//2
    a1 = a[0:m]
    a2 = a[m:]
    mergeSort(a1)
    mergeSort(a2)
    merge(a1, a2, a)
def merge(a1,a2,a):
    i = 0
    j = 0
    k = 0
    while(i < len(a1) & j < len(a2)):
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
    while(j<len(a1)):
        a[k] = a2[j]
        j+=1
        k+=1
    

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
mergeSort(arr)
print(*arr)

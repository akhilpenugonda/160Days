from sys import stdin
def findDuplicateUsingSort(arr, n) :
    arr.sort()
    i = 0
    while(i < len(arr)):
        if(arr[i] == arr[i+1]):
            return arr[i]
        else:
            i+=1
def findDuplicate(arr, n) :
    #Using
    sumOfN = (n-2)*(n-1)/2
    arrSum = sum(arr)
    return int(arrSum - sumOfN)
    
#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip()) 

while t > 0 :

    arr, n = takeInput()
    print(findDuplicate(arr, n))

    t -= 1
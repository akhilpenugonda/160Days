from sys import stdin
def rotate(arr, n, d):
    d = d%n
    if(d == 0):
        return arr
    i = 0
    j = d-1
    while(i < j):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    i = d
    j = n-1
    while(i < j):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    i = 0
    j = n-1
    while(i < j):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr
#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1
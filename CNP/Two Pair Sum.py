from sys import stdin

def pairSumUsingSortAndTwoPointers(arr, n, num) :
    if(len(arr) == 0):
        return 0
    arr.sort()
    i = 0
    j = len(arr)-1
    count = 0
    while(i < j):
        sum = arr[i] + arr[j]
        if(sum == num):
            count += 1
            continue
            i += 1
            j -= 1
        elif(sum > num):
            j -= 1
        else:
            i += 1
    return count
def pairSum(arr, n, num) :
    #Using Map
    map = [0] * 10000
    count = 0
    for i in arr:
        map[i] += 1
    for i in arr:
        count += map[num - i]
        if(i == (num-i)):
            count -= 1
    return int(count/2)
def pairSum(arr, n, num) :
    #Using Dictionary
    dict = {}
    count = 0
    for i in arr:
        if((num - i) in dict):
            count += dict[(num - i)]
        if(i in dict):
            dict[i] += 1
        else:
            dict[i] = 1
    return count
#taking input using fast I/O method
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


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(pairSum(arr, n, num))

    t -= 1
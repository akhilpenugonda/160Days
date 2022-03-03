from sys import stdin
def binarySearch(a, i, j, k):
    if(j >= i):
        m = i + (j - i)//2
        if(a[m] == k):
            return m
        elif(a[m] > k):

            return binarySearch(a, i, m-1, k)
        else:
            return binarySearch(a, m+1, j, k)
    else:
    	return -1
def countOccurences(arr, n, k):
    itemIndex = binarySearch(arr, 0, n-1, k)
    if(itemIndex == -1):
        return 0
    count = 0
    leftLength,rightLength = itemIndex,itemIndex
    #print(leftLength,rightLength)
    while(leftLength >= 1 and arr[leftLength-1] == k ):
        #print(leftLength,rightLength, "array", arr[leftLength-1])
        leftLength -= 1
    while(rightLength <= n-2 and arr[rightLength+1] == k ):
        rightLength += 1
    return (rightLength-leftLength + 1)

def takeInput() :
	n_x = stdin.readline().strip().split(" ")
	n = int(n_x[0].strip())
	x = int(n_x[1].strip())

	if n == 0 :
		return list(), 0, x

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n, x

#main
arr, n, x = takeInput()
print(countOccurences(arr, n, x))
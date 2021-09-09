#O(nlog(n)) time and O(n) space
def sortedSquaredArrayLambda(array):
    lst = list(map(lambda x: x ** 2, array ))
    return sorted(lst)

def sortedSquaredArrayLoopSquaresPythonic(array):
    lst2 = [i**2 for i in array]
    return sorted(lst2)


#O(n) both time and Space
def sortedSquaredArray(array):
    sampleList = [0 for _ in array]
    l = 0
    end = len(array) - 1 
    r = len(array) - 1 
    while(l <= r):
        if(abs(array[l]) > abs(array[r])):
            sampleList[end] = abs(array[l]) ** 2
            l += 1
            end = end -1
        else:
            sampleList[end] = abs(array[r]) ** 2
            r -= 1
            end = end -1
	return sampleList
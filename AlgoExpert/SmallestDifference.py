#Brute Force
def smallestDifferenceBruteForce(arrayOne, arrayTwo):
    minPair = []
    minDistance = 1000000
    for i in arrayOne:
        for j in arrayTwo:
            if(abs(i - j) < minDistance):
                minDistance = abs(i-j)
                minPair = [i,j]
    return minPair

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    l1 =  0
    l2 = 0
    minPair = []
    minDistance = 1000000
    currentDiff = 0
    while(l1 < len(arrayOne) and l2 < len(arrayTwo)):
        firstNum = arrayOne[l1]
        secondNum = arrayTwo[l2]
        diff = firstNum - secondNum
        if(diff == 0):
            minPair = [firstNum, secondNum]
            return minPair
        else:
            if(firstNum > secondNum):
                currentDiff = firstNum - secondNum
                l2 += 1
            else:
                currentDiff = secondNum - firstNum
                l1 += 1
            if(minDistance > currentDiff):
                minDistance = currentDiff
                minPair = [firstNum, secondNum]

    return minPair
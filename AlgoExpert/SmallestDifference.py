#Brute Force
import math
def smallestDifference(arrayOne, arrayTwo):
    minPair = []
    minDistance = 1000000
    for i in arrayOne:
        for j in arrayTwo:
            if(abs(i - j) < minDistance):
                minDistance = abs(i-j)
                minPair = [i,j]
    return minPair
#iterate once to get only peaks using [1,2,1] three elements peaks
def longestPeak(array):
    longestPeak = 0
    startIndex = 1
    if(len(array) == 0 or len(array) == 1 or len(array) == 2):
        return longestPeak
    while startIndex < len(array) - 1:
        isPeak = array[startIndex - 1] < array[startIndex] and array[startIndex] > array[startIndex + 1]
        if not isPeak:
            startIndex += 1
            continue
        leftBottom = startIndex - 2
        while(leftBottom >= 0 and array[leftBottom] < array[leftBottom + 1]):
            leftBottom -= 1
        rightBottom = startIndex + 2
        while(rightBottom <= len(array) - 1 and array[rightBottom] < array[rightBottom - 1]):
            rightBottom += 1
        longestPeak = max(longestPeak, rightBottom - leftBottom - 1)
        startIndex += 1
    return longestPeak

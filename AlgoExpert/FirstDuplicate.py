def firstDuplicateValue(array):
    ret = -1
    minimumIndex = len(array)
    for i in range(len(array) - 1):
        for j in range(i+1, len(array)):
            if(array[i] == array[j] and j < minimumIndex):
                minimumIndex = j
                ret = 1
            else:
                continue
    if(ret != -1):
        return array[minimumIndex]
    else:
        return -1


def firstDuplicateValue(array):
    seen = set()
    for i in range(len(array)):
        if array[i] not in seen:
            seen.add(array[i])
        else:
            return array[i]
    return -1

def firstDuplicateValue(array):
    for i in array:
        absValue = abs(i)
        if array[absValue - 1] < 0:
            return absValue
        array[absValue - 1] *= -1
    return -1


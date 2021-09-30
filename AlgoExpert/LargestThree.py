def findThreeLargestNumbers(array):
    returnArray = [None, None, None]
    for i in array:
        UpdateLargest(returnArray, i)
    return returnArray

def UpdateLargest(returnArray, number):
    if(returnArray[2] is None or number > returnArray[2]):
        ShiftAndUpdate(returnArray, number, 2)
    elif(returnArray[1] is None or number > returnArray[1]):
        ShiftAndUpdate(returnArray, number, 1)
    elif(returnArray[0] is None or number > returnArray[0]):
        ShiftAndUpdate(returnArray, number, 0)
    

def ShiftAndUpdate(returnArray, value, idx):
    for i in range(idx +1):
        if i == idx:
            returnArray[i] = value
        else:
            returnArray[i] = returnArray[i+1] 

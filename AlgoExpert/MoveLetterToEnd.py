def moveElementToEnd(array, toMove):
    l = len(array)-1
    end = len(array)-1
    initial = 0
    while initial < end:
        while initial < end and  array[end] == toMove:
            end -= 1
        if(array[initial] == toMove):
            array[initial], array[end] = array[end], array[initial]
        initial += 1
    return array
print(moveElementToEnd([1,2,3,4,5,2,2,2],2))
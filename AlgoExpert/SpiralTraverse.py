def spiralTraverseMain(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startColumn, endColumn = 0, len(array[0]) - 1
    while(startRow <= endRow and startColumn <= endColumn):
        for col in range(startColumn, endColumn + 1):
            result.append(array[startRow][col])
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endColumn])
        for col in reversed(range(startColumn, endColumn)):
            if(startRow == endRow):
                break
            result.append(array[endRow][col])
        for row in reversed(range(startRow + 1, endRow )):
            if(startColumn == endColumn):
                break
            result.append(array[row][startColumn])
        startColumn += 1
        startRow += 1
        endColumn -= 1
        endRow -= 1
        print(result)
    print(result)
    return result

def spiralTraverse(array):
    result = []
    recursiveSpiral(array, 0, len(array)-1, 0, len(array[0])-1, result)
    return result

def recursiveSpiral(array, startRow, endRow, startColumn, endColumn, result):

    if(startRow > endRow or startColumn > endColumn):
        return
    for col in range(startColumn, endColumn + 1):
        result.append(array[startRow][col])
    for row in range(startRow + 1, endRow + 1):
        result.append(array[row][endColumn])
    for col in reversed(range(startColumn, endColumn)):
        if(startRow == endRow):
            break
        result.append(array[endRow][col])
    for row in reversed(range(startRow + 1, endRow )):
        if(startColumn == endColumn):
            break
        result.append(array[row][startColumn])
    recursiveSpiral(array, startRow + 1, endRow - 1, startColumn + 1, endColumn - 1, result)


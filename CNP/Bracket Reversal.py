
from sys import stdin

def countBracketReversals(inputString) :
    if(len(inputString) == 0):
        return 0
    bracketStack = []
    count = 0
    for i in list(inputString):
        if(i == "{"):
            bracketStack.append(i)
        else:
            if(len(bracketStack) == 0):
                bracketStack.append(i)
            elif(bracketStack[-1] == "{"):
                bracketStack.pop()
            else:
                bracketStack.append(i)
    if(len(bracketStack) % 2 != 0):
        return -1
    else:
        while(len(bracketStack) > 0):
            top = bracketStack.pop()
            top2 = bracketStack.pop()
            if(top == top2):
                count += 1
            else:
                count += 2
    return count
            

print(countBracketReversals(stdin.readline().strip()))

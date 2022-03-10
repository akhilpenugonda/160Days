
from sys import stdin

def checkRedundantBrackets(expression) :
    expression = list(expression)
    expression.reverse()
    if(len(expression) < 0):
        return False
    resp = False
    inputStack = []
    foundBlock = False
    while(len(expression) > 0):
        record = expression.pop()
        #print(4,expression)
        
        if(record != ")"):
            foundBlock = False
            #print(inputStack, expression)
            #print("Appending", record, inputStack)
            inputStack.append(record)
            #print("Appended", record, inputStack)
        else:
            #print("Appended Inputs", record, inputStack)
            #print(5,inputStack)
            inputStack = previousStringHelper(inputStack)
            #print(6,inputStack)
            if(len(inputStack) > 0 and inputStack[-1] == "("):
                return True
            if(len(expression) > 0):
                foundBlock = True
            elif(len(inputStack) == 0 and len(expression) == 0 and not foundBlock):
                return True
            
            
            
    return False
            
                    
def previousStringHelper(inputStack):
    count = 0
    #print(1,inputStack)
    while(len(inputStack) > 0):
        if(inputStack[-1] != "("):
            #print(2,inputStack)
            inputStack.pop()
            count += 1 
        else:
            if(count > 0):
                #print(3,inputStack)
                inputStack.pop()
                return inputStack
    return inputStack

#main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")
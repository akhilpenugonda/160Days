#{}()
#{()}
#{{{()}}}
#{(}) X-Wrong
#Example {(a=b) + (c + d) + e}
#given only ( or ) exists

from sys import stdin
from StackWithLL import Stack
def isBalanced(expression) :
    stack = Stack()
    for i in expression:
        if(i in ["("]):
            stack.push("(")  
            #print(i)
            continue
        elif(i in [")"]):
            if(stack.isEmpty()):
                return False
            top = stack.pop()
            if(top in ["("]):
                continue
            else:
                return False
    if(stack.isEmpty()):
        return True
    else: 
        return False

expression = stdin.readline().strip()

if isBalanced(expression) :
	print("true")

else :
	print("false")



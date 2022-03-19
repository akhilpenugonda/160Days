## Read input as specified in the question.
## Print output as specified in the question.
# Problem ID 328 Midpoint LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def nextNumberHelperUsingIsItNine(head):
    isItNine = False
    if(head.next is not None):
        isItNine = nextNumberHelperUsingIsItNine(head)
        if(isItNine):
            if(head.data == 9):
                head.data = 0
                isItNine = True
                return isItNine
            else:
                head.data += 1
                isItNine = False
                return isItNine
        return isItNine
    else:
        if(head.data == 9):
            head.data = 0
            isItNine = True
            return isItNine
        else:
            head.data += 1
            isItNine = False
            return isItNine
    
    
    

def nextNumber(head):
    tempHeadData = head.data
    if(head is None):
        return head
    
    nextNumberHelperUsingIsItNine(head)
    if(head.data != tempHeadData):
        if(head.data == 0):
            newNode = Node(1)
            newNode.next = head
            head = newNode
            
    return head
    
        
    
        
    #Implement Your Code here
	
    
    pass
        
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head is not None:
        print(head.data,end= ' ')
        head = head.next
    return

# Main
# Read the link list elements including -1
arr=[int(ele) for ele in input().split()]
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
head = nextNumber(l)
printll(head)
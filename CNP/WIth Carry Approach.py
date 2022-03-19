## Read input as specified in the question.
## Print output as specified in the question.
# Problem ID 328 Midpoint LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def nextNumberHelper(head):
    if(head is None):
        return 1
    res = head.data + nextNumberHelper(head.next)
    head.data = int(res%10)
    return int(res/10)
    
    
    

def nextNumber(head):
    if(head is None):
        return head
    
    resp = nextNumberHelper(head)
    if(resp == 1):
        newNode = Node(1)
        newNode.next = head
        head = newNode
            
    return head
    
def addWithCarry(head):
 
    # If linked list is empty, then
    # return carry
    if (head == None):
        return 1
 
    # Add carry returned be next node call
    res = head.data + addWithCarry(head.next)
 
    # Update data and return new carry
    head.data = int((res) % 10)
    return int((res) / 10)
 
# This function mainly uses addWithCarry().
def addOne(head):
 
    # Add 1 to linked list from end to beginning
    carry = addWithCarry(head)
 
    # If there is carry after processing all nodes,
    # then we need to add a new node to linked list
    if (carry != 0):
     
        newNode = Node(0)
        newNode.data = carry
        newNode.next = head
        return newNode # New node becomes head now
     
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
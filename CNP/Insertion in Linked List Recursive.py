from sys import stdin , setrecursionlimit
setrecursionlimit(10**6)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head

def insertAtIR(head, i, data):
    if(i == 0):
        newNode = Node(data)
        newNode.next = head
        return newNode
    if(head is None):
        return None
    if(i < 0 or i > LengthOfLL(head)):
        return head 
    smallHead = insertAtIR(head.next, i-1, data)
    head.next = smallHead
    return head
def LengthOfLL(head):
    count = 0
    while(head):
        count+=1
        head = head.next
    return count
# To print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()

def lengthRecursive(head):
	return (LinkedListLengthRec(head, 0))
def LinkedListLengthRec(head, l):
    if(head):
        return(LinkedListLengthRec(head.next, l+1))
    else:
        return l










# Main
t = int(stdin.readline().rstrip())

while t > 0 :
    head = takeInput()
    ans=lengthRecursive(head)
    print(ans)
    t -= 1 
from sys import stdin

# Following is the Node class already written for the Linked List.
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def deleteNode(head, pos) :
    #print(LengthOfLL(head))
    if(pos < 0 or pos >= LengthOfLL(head)):
        return head
    count = 0
    curr = head
    prev = None
    
    while count < pos:
        prev = curr
        curr = curr.next
        count += 1
    
    if(prev is not None):
        prev.next = curr.next
    else:
        head = head.next
    #NewNode.next = curr

    return head

def insertAtI(head, pos, d):
    #print(LengthOfLL(head))
    if(pos < 0 or pos > LengthOfLL(head)):
        return head
    count = 0
    curr = head
    prev = None
    while count < pos:
        prev = curr
        curr = curr.next
        count += 1
    NewNode = Node(d)
    if(prev is not None):
        prev.next = NewNode
    else:
        head = NewNode
    NewNode.next = curr

    return head

def LengthOfLL(head):
    count = 0
    while(head):
        count+=1
        head = head.next
    return count


# Taking Input Using Fast I/O.
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

# To print the linked list.
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


# Main.
t = int(stdin.readline().strip())

while t > 0 :
    
    head = takeInput()
    pos = int(stdin.readline().rstrip())
    
    head = deleteNode(head, pos)
    printLinkedList(head)

    t -= 1

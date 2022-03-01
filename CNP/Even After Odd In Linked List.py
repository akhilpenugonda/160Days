from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


def evenAfterOdd(head) :
    if(head is None):
        return head
    evenList, oddList = None, None
    evenListHead = None
    evenListTail = None
    oddListHead = None
    oddListTail = None
    
    while(head):
        if(head.data %2 == 0):
            if(evenListHead is None):
                evenListHead = head
                evenListTail = head
                head = head.next
            else:
                evenListTail.next = head
                evenListTail = evenListTail.next
                head = head.next
        else:
            if(oddListHead is None):
                oddListHead = head
                oddListTail = head
                head = head.next
            else:
                oddListTail.next = head
                oddListTail = oddListTail.next
                head = head.next
    if oddListTail==None:
        return evenListHead
    else:
        oddListTail.next=None
    if evenListTail==None:
        return oddListHead
    else:
        evenListTail.next=None
    oddListTail.next = evenListHead
    return oddListTail
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


#to print the linked list 
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)  
    
    t -= 1
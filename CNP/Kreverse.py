from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def kReverse(head, k) :
    tempK = k
    if(k == 0 or k < 0 or k == 1):
        return head
    if(head is None):
        return head
    curr = head
    while(k > 1):
        if(curr is None):
            return head
        curr = curr.next
        k -= 1
    if(curr is None):
        newReverse, tail = reverseLL(head)
        return newReverse
    NonReversepart = curr.next
    curr.next = None
    newReverse, tail = reverseLL(head)
    tail.next = kReverse(NonReversepart, tempK)
    return newReverse
    
        
    
def reverseLL(head):
    prev = None
    tail = head
    curr = head
    while(curr):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev, head
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
def printLinkedList(head) :
    while head is not None:
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    k = int(stdin.readline().strip())

    newHead = kReverse(head, k)
    printLinkedList(newHead)

    t -= 1
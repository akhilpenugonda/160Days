from sys import stdin
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
def LengthOfLL(head):
    count = 0
    while(head):
        count+=1
        head = head.next
    return count
def appendLastNToFirst(head, n) :
    if(n == 0):
        return head
    p1head = None
    p1tail = None
    length = LengthOfLL(head)
    if(length < 1):
        return head
    diff = length - n
    while(diff > 0):
        node = Node(head.data)
        head = head.next
        if(p1head is None):
            p1head = node
            p1tail = node
        else:
            p1tail.next = node
            p1tail = p1tail.next
        diff -= 1
    headCurr = head
    while(headCurr.next):
        headCurr = headCurr.next
    headCurr.next = p1head
    return head
        
        
    
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
            tail = tail.next

        i += 1

    return head


#to print the linked list 
def printLL(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()

#main
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    n = int(stdin.readline().rstrip())

    head = appendLastNToFirst(head, n)
    printLL(head)

    t -= 1 
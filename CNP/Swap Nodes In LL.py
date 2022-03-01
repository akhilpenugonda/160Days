from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None



def swapNodes(head, i, j) :
    p1, a1, n1 = None, None, None
    p2, a2, n2 = None, None, None
    if(i < 0):
        return head
    if(j > (LengthOfLL(head)-1)):
        return head
    if(i == j):
        return head
    curr = head
    k = 0
    while(curr):
        if(k == 0 and k == i):
            p1 = None
            a1 = curr
            #n1 = curr.next
            curr = curr.next
            k += 1
            continue
        if(k == i-1):
            p1 = curr
            a1 = curr.next
            #n1 = curr.next.next
            curr = curr.next
            k += 1
            continue
        if(k == j-1):
            p2 = curr
            a2 = curr.next
            #printLinkedList(a2)
            #n2 = curr.next.next
            curr = curr.next
            k += 1
            continue
        curr = curr.next
        k += 1
        
	#Swapping Start
    #Swap connection 
    p1Temp = p1.next
    p1.next = p2.next
    p2.next = p1Temp
    a1Temp = a1.next
    a1.next = a2.next
    a2.next = a1Temp
    return head
def LengthOfLL(head):
    l = 0
    while(head):
        l += 1
        head = head.next
    return l

#Taking Input Using Fast I/O
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

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    i_j = stdin.readline().strip().split(" ")

    i = int(i_j[0])
    j = int(i_j[1])

    newHead = swapNodes(head, i, j)
    printLinkedList(newHead)

    t -= 1
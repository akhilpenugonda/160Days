from sys import maxsize, stdin
from tempfile import tempdir
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def swapNodes(nodeA, nodeB):
    temp = nodeB.next
    nodeB.next = nodeA
    nodeA.next = temp
    return nodeB
def lengthOfLL(head):
    l = 0
    while(head):
        head = head.next
        l +=1 
    return l
#Bring Largest to top
#Did not Work

def bubbleSortWithNode(mainHead: Node) :
    lengthOfList = lengthOfLL(mainHead)
    mainSorter = 0
    while(mainSorter < lengthOfList-1):
        head = mainHead
        swapped = 0
        maxMover = mainSorter+1
        while(maxMover < lengthOfList):
            if(head.data > head.next.data):
                head = swapNodes(head, head.next)
                swapped = 1
                maxMover += 1
            else:
                maxMover += 1
            head = head.next
        mainSorter += 1
        if(swapped):
            break
    return mainHead
def bubbleSort(head):
    curr=head
    index=Node(None)
    if head is None:
        return 
    while curr.next!=None:
        index=curr.next 
        while index!=None:
            if index.data<curr.data:
                curr.data, index.data = index.data, curr.data
            index=index.next 
        curr=curr.next 
    return head  
def bubbleSortWithNodes(head: Node):
    n = lengthOfLL(head)
    for i in range(n-1):
        prev = None
        curr = head
        for j in range(n-i-1):
            if(curr.data <= curr.next.data):
                prev = curr
                curr = curr.next
            else:
                #All Swaappings are done here
                if(prev is None):
                    temp = curr.next
                    head = head.next
                    curr.next = temp.next
                    temp.next = curr
                    prev = temp
                else:
                    temp = curr.next
                    prev.next = temp
                    curr.next = temp.next
                    temp.next = curr
                    prev = temp
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
            tail = newNode

        i += 1

    return head



def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)
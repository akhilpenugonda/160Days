from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def merge(head1, head2):
    finalHead = None
    finalTail = None
    if(head1 is None):
        return head2
    if(head2 is None):
        return head1
    while(head1 is not None and head2 is not None):
        if(head1.data < head2.data):
            if(finalTail is None):
                finalTail = head1
                finalHead = head1
                head1 = head1.next
            else:
                finalTail.next = head1
                finalTail = finalTail.next
                head1 = head1.next
        else:
            
            if(finalTail is None):
                finalTail = head2
                finalHead = head2
                head2 = head2.next
            else:
                finalTail.next = head2
                finalTail = finalTail.next
                head2 = head2.next
    if(head1 is None and head2 is None):
        return finalHead
    if(head1 is not None):
        finalTail.next = head1
    if(head2 is not None):
        finalTail.next = head2
    return finalHead
def midOfList(head):
    if head is None:
        return head
    slow,fast = head, head
    while fast.next is not None and fast.next.next is not None:
        slow=slow.next
        fast=fast.next.next
    return slow
    
def mergeSort(head) :
    if(head is None or head.next is None):
        return head
    printLinkedList(head)
    mid = midOfList(head)
    half1 = head
    half2 = mid.next
    mid.next = None
    printLinkedList(half1)
    printLinkedList(half2)
    newHead1 = mergeSort(half1)
    newHead2 = mergeSort(half2)
    finalHead = merge(newHead1, newHead2)
    return finalHead



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

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1
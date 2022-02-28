# Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()
def takeInput(listInput):
    num = list(map(int, listInput.split()))
    head = None
    tail = None
    i = 0
    while(i < len(num) and num[i] != -1):
        node = Node(num[i])
        if(head):
            tail.next = node
            tail = node
        else:
            head = node
            tail = node
        i += 1
    return head
def findNode(head, num, pos) :
    if(head is None):
        return -1
    if(num == head.data):
        return pos
    return findNode(head.next, num, pos+1)
cases = int(input())
for i in range(cases):
    l1 = input()
    num = int(input())
    head = takeInput(l1)
    #printLinkedList(head)
    print(findNode(head, num, 0))
    
            


    
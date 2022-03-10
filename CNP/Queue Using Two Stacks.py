from sqlalchemy import false


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#Just for Practice
class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0
    def isEmpty(self):
        return (self.__count == 0)
    def top(self):
        if(self.__count > 0):
            return self.__head.data
        return -1
    def push(self, data):
        if(self.__head is None):
            newNode = Node(data)
            self.__head = newNode
            self.__count += 1
        else:
            newNode = Node(data)
            newNode.next = self.__head
            self.__head = newNode
            self.__count += 1
    def pop(self):
        if(self.isEmpty()):
            return -1
        else:
            data = self.__head.data
            self.__head = self.__head.next
            self.__count -= 1
            return data
    def top(self):
        if(self.isEmpty()):
            return -1
        else:
            return self.__head.data
    
class QueueUsingTwoStacks:
    #Dequeue is O(1)
    def __init__(self):
        self.__s1 = [] 
        self.__s2 = []
    def enqueue(self, data):
        while(len(self.__s1) != 0):
            self.__s2.append(self.__s1.pop())
        self.__s1.append(data)
        while(len(self.__s2) != 0):
            self.__s1.append(self.__s2.pop())
        return
    def dequeue(self):
        if(len(self.__s1) == 0):
            return -1
        else:
            return self.__s1.pop()
    def size(self):
        return len(self.__s1)
    def count(self):
        pass
    def isEmpty(self):
        return len(self.__s1) == 0
    def front(self):
        if(self.isEmpty()):
            return -1
        else:
            return self.__s1[-1]
   
q = QueueUsingTwoStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(8) 
q.dequeue()
print(q)
print(q.isEmpty())
while (q.isEmpty() is False):
    print(q.front())
    q.dequeue()
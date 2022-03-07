from sys import stdin

class Node :
    
    def __init__(self, data) :
        self.data = data
        self.next = None


class Stack :
    #initialize init and other methods
    def __init__(self):
        self.__head = None
        self.__count = 0


    '''----------------- Public Functions of Stack -----------------'''


    def getSize(self) :
        return self.__count
        #Implement the getSize() function



    def isEmpty(self) :
        if(self.__count):
            return False
        else:
            return True
        #Implement the isEmpty() function



    def push(self, data) :
        self.__count += 1
        NewNode = Node(data)
        NewNode.next = self.__head
        self.__head = NewNode
        #Implement the push(element) function



    def pop(self) :
        if(self.isEmpty()):
            return -1
        topNode = self.__head
        self.__head = self.__head.next
        self.__count -= 1
        return topNode.data
        #Implement the pop() function



    def top(self) :
        if(self.isEmpty()):
            return -1
        return self.__head.data
        #Implement the top() function
        


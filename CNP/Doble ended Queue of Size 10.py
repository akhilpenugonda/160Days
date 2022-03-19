## Read input as specified in the question.
## Print output as specified in the question.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class QueueUsingArray:
    def __init__(self):
        self.queue = []
        self.count = 0
    def insertFront(self, data):
        if(self.count == 10):
            print(-1)
            return -1
        
        self.queue = [data] + self.queue
        self.count += 1
    def insertRear(self, data):
        if(self.count == 10):
            print(-1)
            return -1
        self.queue.append(data)
        self.count += 1
    def deleteFront(self):
        if(self.count == 0):
            print(-1)
            return -1
        front = self.queue[0]
        self.queue = self.queue[1:]
        self.count -= 1
        return
    def deleteRear(self):
        if(self.count == 0):
            print(-1)
            return -1
        
        self.queue.pop()
        self.count -= 1
        return 
    def getFront(self):
        if(self.count == 0):
            print(-1)
            return -1
        print(self.queue[0])
        return self.queue[0]
    def getRear(self):
        if(self.count == 0):
            print(-1)
            return -1
        print(self.queue[-1])
        return self.queue[-1]
    
    
    
newQueue = QueueUsingArray()
dataIn = [int(x) for x in input().split(" ")]
i = 0
while(dataIn[i] != -1):
    #print(dataIn)
    #print(i)
    #print(newQueue.queue)
    if(dataIn[i] == 1):
        i += 1
        newQueue.insertFront(dataIn[i])
        i += 1
        continue
    if(dataIn[i] == 2):
        i += 1
        newQueue.insertRear(dataIn[i])
        i += 1
        continue
    if(dataIn[i] == 3):
        i+=1
        newQueue.deleteFront()
        continue
    if(dataIn[i] == 4):
        i+=1
        newQueue.deleteRear()
        continue
    if(dataIn[i] == 5):
        i+=1
        newQueue.getFront()
        continue
    if(dataIn[i] == 6):
        i+=1
        newQueue.getRear()
        continue
    if(dataIn[i] == -1):
        i+=1
        break
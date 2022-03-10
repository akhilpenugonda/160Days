
from sys import stdin
import queue

class Stack :

	#Define data members and __init__()
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
    def getSize(self) :
        return self.q1.qsize()
    def isEmpty(self) :
        return self.q1.qsize() == 0
    def push(self, data) :
        self.q1.put(data)
        return
    def pop(self) :
        if(self.q1.qsize() == 0):
            return -1
        else:
            while(self.q1.qsize() != 0):
                self.q1.put(self.q1.get())
            data = self.q2.get()
            while(self.q2.qsize() != 0):
                self.q1.put(self.q2.get())
            return data
    def top(self) :
        pass

q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

	inputs = stdin.readline().strip().split(" ")
	choice = int(inputs[0])

	if choice == 1 :
		data = int(inputs[1])
		stack.push(data)

	elif choice == 2 :
		print(stack.pop())

	elif choice == 3 :
		print(stack.top())

	elif choice == 4 : 
		print(stack.getSize())

	else :
		if stack.isEmpty() :
			print("true")
		else :
			print("false")

	q -= 1
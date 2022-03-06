#Inbuilt stack is a list
#[1,2,3,4,5]
import queue
q = queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
while not q.empty():
    print(q.get())
stack = queue.LifoQueue()
q.put(1)
q.put(2)
while not q.empty():
    print(q.get())
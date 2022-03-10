
from sys import stdin
import queue

def reverseKElements(inputQueue, k) :
    kReverseHelper(inputQueue, k)
    for i in range(inputQueue.qsize()-k):
        record = inputQueue.get()
        inputQueue.put(record)
    return inputQueue
def kReverseHelper(inputQueue, k):
    if(k > 0):
        data = inputQueue.get()
        kReverseHelper(inputQueue, k-1)
        inputQueue.put(data)
        
#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Takes a list as a stack and returns the element at the top
def top(stack) :
    #assuming the stack is never empty
    return stack[len(stack) - 1]



def takeInput():
    n_k = list(map(int, stdin.readline().strip().split(" ")))
    n = n_k[0]
    k = n_k[1]

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return k, qu


#main
k, qu = takeInput()

qu = reverseKElements(qu, k)

while not qu.empty() :
    print(qu.get(), end = " ")

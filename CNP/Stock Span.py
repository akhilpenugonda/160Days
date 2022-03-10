
from ast import While
from inspect import stack
from sys import stdin

def stockSpan(price, n) :
	#the n square approach
    resp = [0] * n
    Stack = []
    for i in range(len(price)):
        if(len(Stack) == 0):
            resp[i] = 1
            Stack.append(i)
            continue
        if(price[i] > price[Stack[-1]]):
            while(Stack):
                if(price[i] > price[Stack[-1]]):
                    top = Stack.pop()
                    resp[i] += resp[top]
                else:
                    break
            resp[i] += 1
            Stack.append(i)
        else:
            resp[i] += 1
            
            Stack.append(i)
    return resp


def printList(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = " ")

	print()


def takeInput():
	size = int(stdin.readline().strip())

	if size == 0 :
		return list(), 0

	price = list(map(int, stdin.readline().strip().split(" ")))

	return price, size


#main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)

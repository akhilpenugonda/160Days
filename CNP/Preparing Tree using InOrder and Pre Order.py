from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def buildTree(preOrder, inOrder, n) :
    if(len(preOrder) == 0):
        return None
    rootData = preOrder[0]
    root = BinaryTreeNode(rootData)
    rootIndexInInOrder = -1
    for i in range(0, len(inOrder)):
        if inOrder[i] == rootData:
            rootIndexInInOrder = i
            break
    if(rootIndexInInOrder == -1):
        return None
    leftInOrder = inOrder[0:rootIndexInInOrder]
    rightInOrder = inOrder[rootIndexInInOrder+1:]
    lenLeftSubTree = len(leftInOrder)
    leftPreOrder = preOrder[1:lenLeftSubTree+1]
    rightPreOrder = preOrder[lenLeftSubTree+1:]
    leftChild = buildTree(leftPreOrder, leftInOrder, len(leftInOrder))
    rightChild = buildTree(rightPreOrder, rightInOrder, len(rightInOrder))
    root.left = leftChild
    root.right = rightChild
    return root



































'''-------------------------- Utility Functions --------------------------'''

def printLevelWise(root):
    if root is None :
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty(): 
        frontNode = pendingNodes.get()
    
        if frontNode is None :
            print()
            
            if not pendingNodes.empty() :
                pendingNodes.put(None)
                
        else :
            print(frontNode.data, end = " ")
            
            if frontNode.left is not None :
                pendingNodes.put(frontNode.left)
                
                
            if frontNode.right is not None :
                pendingNodes.put(frontNode.right)


                

#Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), list(), 0

    preOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return preOrder, inOrder, n


# Main
preOrder, inOrder, n = takeInput()
root = buildTree(preOrder, inOrder, n)
printLevelWise(root)
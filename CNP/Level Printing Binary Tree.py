from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printNode(root):
    if(root is None):
        return
    print(str(root.data) + ":", end = "")
    lNodeData = ""
    rNodeData = ""
    if(root.right is not None):
        rNodeData = "R:" + str(root.right.data)
    else:
        rNodeData = "R:-1"
    if(root.left is not None):
        lNodeData = "L:" + str(root.left.data)
    else:
        lNodeData = "L:-1"
    print(lNodeData, end = ",")
    print(rNodeData)
    return
def printLevelWise(root):
    # Your code goes here
    q = queue.Queue()
    if(root is None):
        return 
    q.put(root)
    while(not(q.empty())):
        node = q.get()
        printNode(node)
        if(node.left is not None):
            q.put(node.left)
        if(node.right is not None):
            q.put(node.right)
    return
        































    



#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root


# Main
root = takeInput()
printLevelWise(root)
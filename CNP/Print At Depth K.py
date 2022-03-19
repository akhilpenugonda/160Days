from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def height(root) :
	#Your code goes here
    if(root is None):
        return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    return 1 + max(leftHeight, rightHeight)
def findNumberOfLeafNodes(root):
    if(root is None):
        return 0
    if(root.left is None and root.right is None):
        return 1
    leftLeaves = findNumberOfLeafNodes(root.left)
    rightLeaves = findNumberOfLeafNodes(root.right)
    return (leftLeaves + rightLeaves)
def printAtDepthK(root, k):
    if(root is None):
        return
    if(k == 0):
        print(root.data, end = " ")
        return
    printAtDepthK(root.left, k-1)
    printAtDepthK(root.right, k-1)
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

h = height(root)
print(h)
#print(findNumberOfLeafNodes(root))
printAtDepthK(root, 2)
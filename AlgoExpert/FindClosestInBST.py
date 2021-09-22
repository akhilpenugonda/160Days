def findClosestValueInBst(tree, target):
    return traverseAndReturn(tree, target, tree.value)

def traverseAndReturn(tree, target, nearest):
    if tree is None:
        return nearest
    if(abs(target - nearest) > abs(target - tree.value)):
        nearest = tree.value
    if(target < tree.value):
        return traverseAndReturn(tree.left, target, nearest)
    elif(target > tree.value):
        return traverseAndReturn(tree.right, target, nearest)
    else:
        return nearest
    
#You can rely on None since it is a BST if we get None the traverse is done
def findClosestValueInBstHelper(tree, target, nearest):
    currentNode = tree.value
    while currentNode is not None:
        if(abs(target - nearest) > abs(target - currentNode.value)):
            nearest = currentNode.value
        if(target < currentNode.value):
            currentNode = currentNode.left
        elif(target > currentNode.value):
            currentNode = currentNode.right
        else:
            break
    return nearest


#This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def invertBinaryTree(tree):
    invert(tree)
    return tree
def invert(tree):
    if (tree) is None:
        return
    if(tree) is not None:
        tree.right, tree.left = tree.left, tree.right
    invert(tree.left)
    invert(tree.right)


def invertBinaryTree(tree):
    treeStack = [tree]
    while len(treeStack) > 0:
        item  = treeStack.pop()
        if item is None:
            continue
        swapTreeElement(item)
        treeStack.append(item.left)
        treeStack.append(item.right)
    return tree
def swapTreeElement(tree):
    tree.left, tree.right = tree.right, tree.left


def invertBinaryTreePracticeWithWhile(tree):
    treeStack = [tree]
    while len(treeStack) > 0:
        item = treeStack.pop()
        if(item) is None:
            continue
        item.left, item.right = item.right, item.left
        treeStack.append(item.left)
        treeStack.append(item.right)
    return tree
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

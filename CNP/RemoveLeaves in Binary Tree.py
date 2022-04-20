#Remove Leaves

from attr import dataclass


class BinaryTreeNode:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None
        
def removeLeaves(root : BinaryTreeNode):
    if(root is None):
        return None
    if(root.left is None and root.right is None):
        return None
    removeLeaves(root.left)
    removeLeaves(root.right)
    return root
 

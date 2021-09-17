class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    sums = []
    calculateBranchSum(root, 0, sums)
    return sums
def calculateBranchSum(node, runningSum, sums):
    if node is None:
        return 
    
    runningSum += node.value
    if(node.left is None and node.right is None):
        sums.append(runningSum)
        return
    calculateBranchSum(node.left, runningSum, sums)
    calculateBranchSum(node.right, runningSum, sums)
    
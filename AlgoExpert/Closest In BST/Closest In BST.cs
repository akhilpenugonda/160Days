using System;

public class Program {
	public static int FindClosestValueInBst(BST tree, int target) 
	{
		return FindClosestValueInBST(tree, target, tree.value);
	}
	public static int FindClosestValueInBST(BST tree, int target, int closest)
	{
		if(Math.Abs(target - closest) > Math.Abs(target-tree.value)){
			closest = tree.value;
		}
		if(target < tree.value && tree.left != null)
		{
			return FindClosestValueInBST(tree.left, target, closest);
		}
		else if(target > tree.value && tree.right != null)
		{
			return FindClosestValueInBST(tree.right, target, closest);
		}
		else
		{
			return closest;
		}
	}

	public class BST {
		public int value;
		public BST left;
		public BST right;

		public BST(int value) {
			this.value = value;
		}
	}
}

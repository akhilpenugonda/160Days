using System;

public class Program {
	public static int[] TwoNumberSum(int[] array, int targetSum) {
		// Two Pointer approach
		Array.Sort(array);
		int left = 0;
		int right = array.Length - 1;
		while(left < right)
		{
			int currentSum = array[left] + array[right];
			if(currentSum == targetSum)
			{
				return new int[] {array[left], array[right]};
			}
			if(currentSum > targetSum)
			{
				right --;
			}
			else if(currentSum < targetSum)
			{
				left ++;
			}
		}
		return new int[0];
	}
}

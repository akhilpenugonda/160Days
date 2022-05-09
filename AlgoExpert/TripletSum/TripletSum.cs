using System;
using System.Collections.Generic;

public class Program {
	public static List<int[]> ThreeNumberSum(int[] array, int targetSum) {
		Array.Sort(array);
		List<int[]> tripletsList = new List<int[]>();
		for (int i = 0; i < array.Length - 2; i++)
		{
			int left = i+1;
			int right = array.Length -1;
			while(left < right)
			{
				int currentSum = array[i] + array[left] + array[right];
				if(targetSum == currentSum)
				{
					int[] newTriplet = {array[i], array[left], array[right]};
					tripletsList.Add(newTriplet);
					left++;
					right--;
				}
				else
					if(currentSum > targetSum)
					{
						right--;
					}
				else
					if(currentSum < targetSum)
					{
						left++;
					}
			}
		}
		return tripletsList;
	}
}


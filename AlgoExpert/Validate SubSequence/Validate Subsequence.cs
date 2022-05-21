using System;
using System.Collections.Generic;

public class Program {
	public static bool IsValidSubsequence(List<int> array, List<int> sequence) {
		// Write your code here.
		int i = 0;
		int j = 0;
		while(i < array.Count && j < sequence.Count)
		{
			if(array[i] == sequence[j])
			{
				j ++;
			}
			i++;
		}
		return j == sequence.Count;
	}
}

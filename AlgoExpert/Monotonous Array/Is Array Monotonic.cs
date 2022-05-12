using System;

public class Program {
	public static bool IsMonotonic(int[] array) {
		var isNonDecreasing = true;
		var isNonIncreasing = true;
		for (int i = 1; i < array.Length; i++)
		{
			if(array[i] < array[i-1])
			{
				isNonDecreasing = false;
			}
			if(array[i] > array[i-1])
			{
				isNonIncreasing = false;
			}
		}
		return isNonIncreasing||isNonDecreasing;
	}
}

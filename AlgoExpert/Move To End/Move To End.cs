using System;
using System.Collections.Generic;

public class Program {
	public static List<int> MoveElementToEnd(List<int> array, int toMove) {
		// Write your code here.
		int i = 0;
		int j = array.Count - 1;
		while(i < j)
		{
			while(j > i && array[j] == toMove)
			{
				j--;
			}
			if(i < j && array[i] == toMove)
			{
				Swap(i,j,array);
			}
			i++;
		}
		return array;
	}
	public static void Swap(int i, int j, List<int> array)
	{
		int temp = array[i];
		array[i] = array[j];
		array[j] = temp;
	}
}

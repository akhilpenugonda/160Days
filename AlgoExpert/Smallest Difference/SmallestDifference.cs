using System;

public class Program {
	public static int[] SmallestDifference(int[] arrayOne, int[] arrayTwo) {
		// Write your code here.
		Array.Sort(arrayOne);
		Array.Sort(arrayTwo);
		int a1ptr = 0;
		int a2ptr = 0;
		int[] smallestDifferencePair = new int[2];
		int minDifference = Int32.MaxValue;
		int current = Int32.MaxValue;
		while(a1ptr < arrayOne.Length && a2ptr < arrayTwo.Length)
		{
			int firstNumber = arrayOne[a1ptr];
			int secondNumber = arrayTwo[a2ptr];
			if(firstNumber > secondNumber)
			{
				current = firstNumber - secondNumber;
				a2ptr++;
			}
			else if(firstNumber < secondNumber)
			{
				current = secondNumber - firstNumber;
				a1ptr++;
			}
			else{
				return new int[] {firstNumber, secondNumber};
			}
			if (current < minDifference)
			{
				minDifference = current;
				smallestDifferencePair = new int[] {firstNumber, secondNumber};
			}
		}
		
		return smallestDifferencePair;
	}
}

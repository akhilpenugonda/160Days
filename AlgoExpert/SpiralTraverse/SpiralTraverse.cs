using System;
using System.Collections.Generic;

//Its like getting the bunch of inner perimeters

public class Program {
	public static List<int> SpiralTraverse(int[,] array) {
		if(array.GetLength(0) == 0) return new List<int>();
		var result = new List<int> ();
		var startRow = 0;
		var endRow = array.GetLength(0) - 1;
		var startCol = 0;
		var endCol = array.GetLength(1) - 1;
		while(startRow <= endRow && startCol <= endCol){
			for(int col = startCol; col <= endCol; col++){
				result.Add(array[startRow, col]);
			}
			for(int row = startRow + 1; row <= endRow; row++){
				result.Add(array[row, endCol]);
			}
			for(int col = endCol - 1; col >= startCol; col --){
				if(startRow == endRow) break;
				result.Add(array[endRow, col]);
			}
			for(int row = endRow - 1; row > startRow; row--){
				if(startCol == endCol) break;
				result.Add(array[row, startCol]);
			}
			startRow ++;
			endRow--;
			startCol++;
			endCol--;
		}
		return result;
	}
}

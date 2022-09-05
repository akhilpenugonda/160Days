using System;
using System.Numerics;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DriverCode
{

    class GFG
    {
        static void Main(string[] args)
        {
            int testcases;// Taking testcase as input
            testcases = Convert.ToInt32(Console.ReadLine());
            while (testcases-- > 0)// Looping through all testcases
            {
                int[,] arr = new int[9,9];
                string s = Console.ReadLine().Trim();
                s = s + " " + "0";
                int k = 0;
                for(int i=0;i<9;i++){
                    for(int j=0;j<9;j++){
                        arr[i,j] = s[k++];
                    }
                }
                Solution obj = new Solution();
                bool res = obj.SolveSudoku(arr);
                if(res == true){
                    obj.printGride(arr);
                }
                else{
                    Console.Write("No solution exists");
                }
          }

        }
    }
}

class Solution
    {
        static int N = 9;
        //Complete this function
        public bool SolveSudoku(int[,] arr){
            return(SolveSudokuHelper(arr, 0, 0));
        }
        public bool SolveSudokuHelper(int[,] arr, int row, int col){
            if(row == N-1 && col == N){
                return true;
            }
            if (col == N){
                row++;
                col = 0;
            }
            if(arr[row, col] != 0){
                return solveSudoku(arr, row, col + 1);
            }
            for (int num = 1; num < 10; num ++){
                if(isSafe(arr, row, col, num)){
                    arr[row, col] = num;
                    if(solveSudoku(arr, row, col+1)){
                        return true;
                    }
                    arr[row, col] = 0;
                    
                }
            }
            return false;
        }
        public void printGrid(int[,] arr){
            //Code Here
            for (int i = 0; i < N; i ++){
                for (int j = 0; j< N; j++){
                    Console.Write(arr[i,j] + " ");
                }
                Console.WriteLine();

            }
        }
        static bool isSafe(int [,] grid, int row, int col, int num){
            for (int x = 0; x <= 8; x++) {
                if(grid[row, x] == num){
                    return false;
                }
            }
            for (int x = 0; x <= 8; x++){
                if(grid[x,col] == num){
                    return false;
                }
            }
            int startRow = row - row % 3, startCol = col - col % 3;
            for (int i = 0; i < 3; i ++){
                for (int j = 0; j < 3; j++){
                    if(grid[i + startRow, j + startCol] == num){
                        return false;
                    }
                }
            }
            return true;
        }

    }
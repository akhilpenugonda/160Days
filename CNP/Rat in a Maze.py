n = int(input())
maze = []
for i in range(n):
    row = [int(ele) for ele in input().split()]
    maze.append(row)

def printPaths(maze):
    n = len(maze)
    solution = [[0 for i in range(n)] for j in range(n)]
    printPathsHelper(0,0,maze,n, solution)
def printPathsHelper(x,y,maze,n,solution):
    if(x == n-1 and y == n-1 and maze[x][y] == 1): # maze[x][y] == 1 Will always be 1 since it is end of the maze
        solution[x][y] = 1
        print(solution)
        return 
    if(x < 0 or y < 0 or x >= n or y >= n or maze[x][y] == 0 or solution[x][y] == 1):
        return
    solution[x][y] = 1
    printPathsHelper(x+1, y, maze, n, solution)
    printPathsHelper(x, y+1, maze, n, solution)
    printPathsHelper(x-1, y, maze, n, solution)
    printPathsHelper(x, y-1, maze, n, solution)
    solution[x][y] = 0
    return
printPaths(maze)
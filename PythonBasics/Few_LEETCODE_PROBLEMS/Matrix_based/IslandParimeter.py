from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        max=0
        k=0
        #boolean[][] isVisited = new boolean[R][C];
        isVisited = [[False for _ in range(C)] for _ in range(R)]

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    return self.getLandsDFS(i,j,isVisited,grid)
        
    def getLandsDFS(self, i: int, j: int, isVisited: List[List[bool]], grid: List[List[int]]) -> int:
         if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:  # If out of bounds or water (0)
            return 1
         if isVisited[i][j]:  # If already visited
            return 0
         
         isVisited[i][j] = True

         return (
            self.getLandsDFS(i - 1, j, isVisited, grid)  # DFS in all four directions
            + self.getLandsDFS(i, j - 1, isVisited, grid)
            + self.getLandsDFS(i, j + 1, isVisited, grid)
            + self.getLandsDFS(i + 1, j, isVisited, grid)
         )
    
    # Example usage
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
solution = Solution()
print(solution.islandPerimeter(grid))  # Output: 16

    

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        line_sum = 0
        ROW_MAX = len(grid)
        COLUMN_MAX = len(grid[0])
        
        for i in range(0,ROW_MAX):
            for j in range(0,COLUMN_MAX):
                if grid[i][j] == 1:
                    line_sum += 4
                    if j > 0 and grid[i][j-1] == 1:
                        line_sum -=1
                    if j < COLUMN_MAX -1 and grid[i][j+1] == 1:
                        line_sum -=1
                    if i > 0 and grid[i-1][j] == 1:
                        line_sum -=1
                    if i < ROW_MAX -1 and grid[i+1][j] == 1:
                        line_sum -=1
        return line_sum

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        
        sum = 0
        for i in range(len(grid)):
            grid[i][0] += sum
            sum = grid[i][0]
            
        sum = 0
        for i in range(len(grid[0])):
            grid[0][i] += sum
            sum = grid[0][i]
            
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j]+= min(grid[i][j-1], grid[i-1][j])
        return grid[-1][-1]
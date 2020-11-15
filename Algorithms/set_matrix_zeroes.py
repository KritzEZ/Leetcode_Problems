class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        zero_cord = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zero_cord.append([i,j])
        
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        for cords in zero_cord:
            for i in range(row_len):
                matrix[i][cords[1]] = 0
            for j in range(col_len):
                matrix[cords[0]][j] = 0
                
        return matrix
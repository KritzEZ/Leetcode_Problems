class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if not matrix:
            return False
        
        for rows in range (len(matrix)):
            if not matrix[rows]:
                return False
            
            if target < matrix[rows][0] and target < matrix[rows][len(matrix[rows])-1]:
                return False
            elif target > matrix[rows][0] and target > matrix[rows][len(matrix[rows])-1]:
                continue
            else:
                for cols in range(len(matrix[rows])):
                    if matrix[rows][cols] == target:
                        return True
                return False
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return 1
        
        lastHolder = [1,1]
        
        for i in range(2, n+1):
            lastHolder.append(lastHolder[i-1] + lastHolder[i-2])
            
        return lastHolder[n]
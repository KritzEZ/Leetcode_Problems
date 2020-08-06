class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        row = 0
        rowlim = 1
        while True:
            n -= rowlim
            if n < 0: break
            row +=1
            if n == 0: break
            rowlim = row +1
            
        return row
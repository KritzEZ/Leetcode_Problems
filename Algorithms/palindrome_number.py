class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0: return False
        
        curX = str(x)
        revX = curX[::-1]
        
        return curX == revX
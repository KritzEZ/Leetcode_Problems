class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        newt = list(t)
        
        for i in range(len(s)):
            if s[i] in newt:
                newt.remove(s[i])
                
            else:
                return s[i]
            
        return newt[0]
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s)==0 or s.isspace(): return 0
        
        splitStr = s.split()
        return len(splitStr[-1])
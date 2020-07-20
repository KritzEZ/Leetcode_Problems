class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        
        strSplit = s.split(" ")
        
        revStr = ""
        
        for i in range(len(strSplit)-1, -1, -1):
            if strSplit[i] != "":
                revStr += strSplit[i] + " "
        
        return revStr[:len(revStr)-1]
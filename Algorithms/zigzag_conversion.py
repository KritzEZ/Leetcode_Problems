class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if len(s) <= numRows:
            return s
        
        ans = [[] for i in range(numRows)]
        
        count = 0
        inc = True
        
        for char in s:
            ans[count] = ''.join(ans[count])+char
            if inc and count < numRows-1:
                count += 1
                inc = True
            elif inc and count == numRows-1:
                count -= 1
                inc = False
            elif not inc and count > 0:
                count -= 1
                inc = False
            elif not inc and count == 0:
                count += 1
                inc = True
                    
        return ''.join(ans)
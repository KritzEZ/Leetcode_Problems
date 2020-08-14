class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev = [1]
        for i in range(rowIndex+1):
            temp = [] 
            
            if i == 0:
                continue
            
            for j in range(i+1):
                if j==0 or j==i:
                    temp.append(1)
                else:
                    temp.append(prev[j-1] + prev[j])
            prev = temp
            
        return prev
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = n
        strNum = str(num)
        holder = [n]
        
        while num != 1:
            added = 0
            strNum = str(num)
            for i in range(len(strNum)):
                added += (int(strNum[i])**2)
            
            num = added
            
            if num in holder:
                return False
            holder.append(num)
        
        return True
                
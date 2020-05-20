def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        strx = str(x)
        
        if strx[0] != "-":
            answer = int(strx[::-1])
        else:
            temp = (strx[1:])[::-1]
            answer = int("-" + temp)
            
        if answer >= 2**31-1 or answer <= -2**31 or x >= 2**31-1 or x <= -2**31: return 0    
        return answer
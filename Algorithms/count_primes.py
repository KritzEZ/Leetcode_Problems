class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2: return 0
        
        count = 0
        
        for i in range(2, n):
            prime = True
            for j in range (2, i//2 +1):
                if i%j == 0:
                    prime = False
                    break
            if prime:
                count += 1
        return count
                    
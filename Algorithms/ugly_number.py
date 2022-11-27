class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ugly = [2,3,5]

        if n<=0:
            return False

        for uglyfactor in ugly:
            while n%uglyfactor==0:
                n=n//uglyfactor

        return (n==1)
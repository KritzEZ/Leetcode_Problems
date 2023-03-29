class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        count = 0
        for i in range (1, (num//2)+1):
            if num%i == 0:
                count += i
        if count == num:
            return True
        else:
            return False
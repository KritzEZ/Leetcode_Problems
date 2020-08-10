class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binaryNum = bin(num)[2:]
        
        binaryNum = binaryNum.replace("1", "2")
        binaryNum = binaryNum.replace("0", "1")
        binaryNum = binaryNum.replace("2", "0")
        
        return int(binaryNum,2)
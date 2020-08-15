class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        sortedNum = sorted(nums)
        
        while i < len(nums)-2:
            if sortedNum[i] == sortedNum[i+2]:
                i+=3
            else:
                return sortedNum[i]
            
        return sortedNum[len(nums)-1]
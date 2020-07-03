class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        sortedNum = sorted(nums)
        
        while i < len(nums)-1:
            if sortedNum[i] == sortedNum[i+1]:
                i+=2
            else:
                return sortedNum[i]
            
        return sortedNum[len(nums)-1]
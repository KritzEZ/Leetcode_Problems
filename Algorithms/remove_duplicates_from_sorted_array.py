class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        counter = 1
        
        if len(nums) == 0: return 0
        
        for i in range (1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[counter] = nums[i]
                counter += 1
                
        return counter
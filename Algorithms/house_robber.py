class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums: return 0
        
        if len(nums) == 1: return nums[0]
        
        temp = nums[1]
        nums[1] = max(nums[0], temp)
        
        for i in range(2,len(nums)):
            temp = nums[i]
            nums[i] = max(nums[i-1], nums[i-2]+temp)
            
        return nums[len(nums)-1]
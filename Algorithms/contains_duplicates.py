class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if not nums: return False
        
        newNums = nums.sort()
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False
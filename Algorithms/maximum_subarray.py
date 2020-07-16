class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum = nums[0]
        higher = nums[0]
        
        for i in range(1,len(nums)):
            higher = max(nums[i], higher+nums[i])
            maxsum = max(maxsum, higher)
        return maxsum
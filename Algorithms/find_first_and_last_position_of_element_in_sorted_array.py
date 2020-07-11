class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums: return [-1, -1]
        
        ans = [-1, -1]
        
        for i in range(len(nums)):
            reverse = len(nums)-1-i
            
            if nums[i] == target and ans[0] == -1:
                ans[0] = i
            if nums[reverse] == target and ans[1] == -1:
                ans[1] = reverse
            
            if -1 not in ans:
                return ans
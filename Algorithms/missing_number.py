class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        total_num = (len(nums) * (len(nums)+1))//2
        
        total_sum = 0
        for num in nums:
            total_sum += num
            
        return total_num - total_sum
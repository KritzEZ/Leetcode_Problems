class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) == 1:
            return 0
        
        back = "less"
        fwd = "less" 
        
        for i in range(len(nums)):
            
            #Checking forward neighbor
            if i != len(nums)-1 and nums[i]>nums[i+1]:
                fwd = "less"
            elif i != len(nums)-1 and nums[i]<nums[i+1]: 
                fwd = "more"
            
            #Checking behind neighbor
            if i!=0 and nums[i]<nums[i-1]:
                back = "more"
            elif i!=0 and nums[i]>nums[i-1]:
                back = "less"
                
            #Checking if element is peak
            if back == fwd == "less":
                return i
            
        #Returning index of higher start/end point
        if nums[0] > nums[len(nums)-1]:
            return 0
        else:
            return len(nums)-1
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        ans = []
        rangeStart = nums[0]
        rangeEnd = nums[0]
        for i in range (1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                rangeEnd = nums[i]
            else:
                if rangeStart == rangeEnd:
                    ans.append(str(rangeStart))
                else:
                    ans.append(str(rangeStart)+"->"+str(rangeEnd))
                rangeStart = rangeEnd = nums[i]
        
        if rangeStart == rangeEnd:
            ans.append(str(rangeStart))
        else:
            ans.append(str(rangeStart)+"->"+str(rangeEnd))

        return ans
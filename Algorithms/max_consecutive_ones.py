class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCount = 0
        currentCount = 0
        prevOne = True
        for i in range(len(nums)):
            if nums[i] == 1 and prevOne:
                currentCount += 1

            elif nums[i] == 1 and not prevOne:
                prevOne = True
                currentCount = 1

            elif nums[i] == 0:
                prevOne = False
                if currentCount > maxCount:
                    maxCount = currentCount
        if currentCount > maxCount:
            maxCount = currentCount

        return maxCount
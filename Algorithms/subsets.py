class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans = []
        self.recurse([], nums, 0)
        return self.ans

    def recurse(self, arr, nums, ind):
        if ind <= len(nums)-1:
            for i in range(ind, len(nums)):
                self.recurse(arr+[nums[i]], nums, i+1)
        self.ans.append(arr)
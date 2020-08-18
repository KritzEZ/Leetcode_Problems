class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        dic = {}
        
        for i, j in enumerate(nums):
            if j in dic and i <= dic[j]:
                return True
            dic[j] = i+k
        return False
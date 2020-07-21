class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = []
        
        def helper(numList, temp=[]):
            if not numList:
                ans.append(temp)
                return
            
            for i in range(len(numList)):
                helper(numList[:i]+numList[i+1:], temp+[numList[i]])
                
        helper(nums)
        
        return ans
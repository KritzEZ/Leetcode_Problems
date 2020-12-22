class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        
        def helper(nums, root=None):
            if len(nums) == 0:
                return None
            else:
                mid = len(nums)//2
                root = TreeNode(val=nums[mid])
                
                root.left = helper(nums[:mid], root)
                root.right = helper(nums[mid+1:], root)
                
                return root
                
        return helper(nums)
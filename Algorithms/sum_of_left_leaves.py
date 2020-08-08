# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.sum = 0
        
        def helper(root):
            if root==None:
                return root
            if root.left and not root.left.left and not root.left.right:
                self.sum += (root.left.val)
            helper(root.left)
            helper(root.right)
        
        helper(root)
        return (self.sum)
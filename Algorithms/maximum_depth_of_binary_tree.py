# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def finder(node):
            if node == None: return 0
            
            left = right = 0
            
            if node.left:
                left = finder(node.left)
            if node.right:
                right = finder(node.right)
                
            return max(left, right) + 1
        
        return finder(root)
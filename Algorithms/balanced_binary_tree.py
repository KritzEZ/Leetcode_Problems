# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        
        def checkDepth(node):
            if not node: return 0
            return max(checkDepth(node.left), checkDepth(node.right))+1
        
        treeLeft = checkDepth(root.left)
        treeRight = checkDepth(root.right)
        
        return self.isBalanced(root.left) and self.isBalanced(root.right) and (abs(treeLeft-treeRight) < 2)
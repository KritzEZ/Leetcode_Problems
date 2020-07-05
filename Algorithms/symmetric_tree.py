# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def sameTree(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            
            return (t1.val == t2.val) and sameTree(t1.left, t2.right) and sameTree(t1.right, t2.left)
        
        return sameTree(root.left, root.right)
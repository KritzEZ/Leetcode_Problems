class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        if not root:
            return None
        else:
            self.helper(root, ans)
        return ans
        
    def helper(self, root, result):
        result.append(root.val)
        
        if root.left:
            self.helper(root.left, result)
            
        if root.right:
            self.helper(root.right, result)
            
        if not root.left and not root.right:
            return result
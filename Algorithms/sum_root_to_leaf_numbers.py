class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        result = self.helper(root, [], 0)
        return sum(result)
    
    def helper(self, root, result, num):
        if not root.left and not root.right:
            result.append(root.val + (num*10))
            return result
        num = root.val + num*10
        if root.left:
            self.helper(root.left, result, num)
        if root.right:
            self.helper(root.right, result, num)
        return result
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root:
            return self.helper([root], [])
        else: 
            return []
        
        
    def helper(self, queue, result):
        next_level = []
        temp = []
        for i in queue:
            temp.append(i.val)
            if i.left:
                next_level.append(i.left)
            if i.right:
                next_level.append(i.right)
        
        result.append(temp)
        if not next_level:
            return result
    
        return self.helper(next_level, result)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def isSameLeaf(p, q):
            
            if p == None and q == None:
                return True
            elif (p == None and q != None) or (p != None and q == None):
                return False
            elif p.val != q.val:
                return False
            
            leftbranch = isSameLeaf(p.left, q.left)
            rightbranch = isSameLeaf(p.right, q.right)
            
            if leftbranch == False:
                return False
            elif rightbranch == False:
                return False
            else: return True
        
        return isSameLeaf(p, q)
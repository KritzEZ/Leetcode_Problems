# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head: return None
        
        ans = None
        
        while head:
            temp = head 
            head = head.next
            
            temp.next = ans
            ans = temp
        return ans
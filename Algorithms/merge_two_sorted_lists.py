# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = ListNode(0)
        ans = head
        
        while True:
            if not l1 and not l2:
                return head.next
            if l1 and not l2:
                ans.next = ListNode(l1.val)
                ans = ans.next
                l1 = l1.next
            
            elif (not l1 and l2):
                ans.next = ListNode(l2.val)
                ans = ans.next
                l2 = l2.next
                
            elif l1.val < l2.val:
                ans.next = ListNode(l1.val)
                ans = ans.next
                l1 = l1.next
            
            else:
                ans.next = ListNode(l2.val)
                ans = ans.next
                l2 = l2.next
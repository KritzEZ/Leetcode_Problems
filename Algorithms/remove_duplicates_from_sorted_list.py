# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        listHolder = ListNode()
        listHolder.next = head
        
        while head:
            nextNum = head.next
            
            while nextNum and nextNum.val == head.val:
                nextNum = nextNum.next
            head.next = nextNum
            head = head.next
        return listHolder.next
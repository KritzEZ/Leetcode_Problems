class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        temp = head
        while temp and temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp =  temp.next
            
        return head
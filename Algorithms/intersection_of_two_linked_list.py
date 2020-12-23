class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def getLen(head):
            headLen = 0
            while head:
                headLen += 1
                head = head.next
            return headLen
        
        lenA = getLen(headA)
        lenB = getLen(headB)
        
        if lenA > lenB:
            for i in range(lenA-lenB):
                headA = headA.next
        if lenB > lenA:
            for i in range(lenB-lenA):
                headB = headB.next
                
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
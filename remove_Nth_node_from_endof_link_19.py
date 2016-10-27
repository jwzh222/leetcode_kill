# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        d = ListNode(None)
        d.next = head
        h = d
        t = d
        
        while( n> 0):
            t = t.next
            n-=1
        while( t.next):
            t=t.next
            h=h.next
        h.next=h.next.next
        return d.next
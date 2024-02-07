# The goal is to remove all nodes with value val from a linked list. => Use dummy node

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        d = ListNode(next= head)

        p, c = d, head

        while c:
            next = c.next

            if c.val == val:
                p.next = next
            else:
                p = c

            c = next

        return d.next
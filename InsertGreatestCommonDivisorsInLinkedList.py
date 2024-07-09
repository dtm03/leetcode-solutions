# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        if not head or not head.next:
            return head

        def gcd(val1, val2):
            while val2:
                val1, val2 = val2, val1 % val2
            return val1

        current = head
        while current and current.next:
            gcd_value = gcd(current.val, current.next.val)
            gcd_node = ListNode(gcd_value, current.next)
            current.next = gcd_node
            current = gcd_node.next

        return head
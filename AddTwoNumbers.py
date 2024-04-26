# Edge cases cuz of carry
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            val = l1.val if l1 else 0
            val += l2.val if l2 else 0
            val += carry

            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next

        return dummy.next
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeNodes(self, head):
        curr = head.next
        tail = head
        total = 0

        while curr:
            if curr.val != 0:
                total += curr.val
            else:
                tail.val = total
                tail.next = curr.next
                tail = tail.next
                total = 0
            curr = curr.next

        return head

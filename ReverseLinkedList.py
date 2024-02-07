# The goal is to reverse a linked list

class Solution(object):
    def reverseList(self, head):

        prev, curr = None, head

        while curr:

            # Save the next node
            nxt = curr.next

            # Reverse the current node
            curr.next = prev

            # Move to the next node
            prev = curr

            # Move to the next node
            curr = nxt

        return prev
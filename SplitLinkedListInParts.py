# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Step 2: Calculate the size of each part
        part_size = length // k
        extra_nodes = length % k

        # Step 3: Split the list
        parts = []
        current = head
        for i in range(k):
            part_head = current
            part_length = part_size + (1 if i < extra_nodes else 0)

            # Traverse part_length nodes in the current part
            for j in range(part_length - 1):
                if current:
                    current = current.next

            # Disconnect the current part from the rest of the list
            if current:
                next_part = current.next
                current.next = None  # End the current part
                current = next_part   # Move to the next part

            # Add the current part's head to the result
            parts.append(part_head)

        return parts
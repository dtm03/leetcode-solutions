class Solution(object):
    def middleNode(self, head):
        curr = head
        counter = 1

        while curr.next:
            curr = curr.next
            counter += 1

        curr = head

        counter /= 2

        while counter > 0:
            curr = curr.next
            counter -= 1

        return curr
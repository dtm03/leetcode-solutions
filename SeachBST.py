# The goal is to search a binary search tree for a given value. => Use iteration

class Solution(object):

    def searchBST(self, root, val):

        while root and root.val != val:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
        return root

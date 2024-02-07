# The goal is to find the maximum depth of a binary tree => Use recursion

class Solution(object):
    def maxDepth(self, root):

        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
class Solution(object):
    def getMinimumDifference(self, root):
        self.prev = float('-inf')
        self.min_diff = float('inf')

        def inorderTraversal(node):
            if not node:
                return

            inorderTraversal(node.left)
            self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorderTraversal(node.right)

        inorderTraversal(root)

        return self.min_diff
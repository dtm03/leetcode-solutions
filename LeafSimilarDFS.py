class Solution(object):
    def leafSimilar(self, root1, root2):

        leaves1 = []
        leaves2 = []

        self.collectLeaves(root1, leaves1)
        self.collectLeaves(root2, leaves2)

        return leaves1 == leaves2

    def collectLeaves(self, node, leaves):

        if node is None:
            return

        if node.left is None and node.right is None:
            leaves.append(node.val)

        self.collectLeaves(node.left, leaves)
        self.collectLeaves(node.right, leaves)
class Solution(object):
    def longestZigZag(self, root):

        def helper(node, isLeft, depth):
            if not node: return depth

            if isLeft:
                depth = max(
                    depth,
                    helper(node.right, False, depth + 1),
                    helper(node.left, True, 0)
                )
            else:
                depth = max(
                    depth,
                    helper(node.right, False, 0),
                    helper(node.left, True, depth + 1)
                )

            return depth

        return max(helper(root.left, True, 0), helper(root.right, False, 0))
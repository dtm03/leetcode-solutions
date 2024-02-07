# Invert a binary tree -> switch the children, call the function recursively for each of the switched children,
# return the root

class Solution(object):
    def invertTree(self, root):

        # Base case: If the root is None, there's nothing to invert
        if root is None:
            return None

        # Swap the left and right subtrees
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the modified root
        return root


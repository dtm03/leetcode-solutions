# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstToGst(self, root):

        self.curr_sum = 0

        def reverse_inorder(node):
            if not node:
                return

            # Traverse the right subtree
            reverse_inorder(node.right)

            # Process the current node
            self.curr_sum += node.val
            node.val = self.curr_sum

            # Traverse the left subtree
            reverse_inorder(node.left)

        reverse_inorder(root)
        return root

# Faster solution:
    class Solution(object):
        def __init__(self):
            self.sum = 0

        def bstToGst(self, root):
            if root:
                self.bstToGst(root.right)  # Traverse the right subtree
                self.sum += root.val  # Update the sum
                root.val = self.sum  # Update the current node's value
                self.bstToGst(root.left)  # Traverse the left subtree
            return root

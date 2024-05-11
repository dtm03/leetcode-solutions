# Find the lowest common ancestor in a BST, meaning the one child is bigger and one is smaller

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

    # Go through the tree until the return-value is found
        while True:

    # Go down the right side if the root is smaller than both children
            if root.val < min(p.val,q.val):
                root = root.right

    # Go down the left side if the root is bigger than both children
            elif root.val > max(p.val,q.val):
                root = root.left

    # Return the root if the split occurs
            else:
                return root
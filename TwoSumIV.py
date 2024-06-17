class Solution(object):
    def findTarget(self, root, k):
        diffs = set()

        def preorder(root):
            if root is None:
                return False
            if root.val in diffs:
                return True
            diffs.add(k - root.val)
            return preorder(root.left) or preorder(root.right)

        return preorder(root)
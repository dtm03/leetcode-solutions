class Solution(object):
    def isSymmetric(self, root):
        return self.isMirror(root, root)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return (left.val == right.val) and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
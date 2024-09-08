class Solution(object):
    def isSubPath(self, head, root):
        # Base case: if root is null, return False
        if not root:
            return False

        # Helper function to perform DFS matching the list with tree
        def dfs(node, head):
            # If the linked list is completely traversed, return True
            if not head:
                return True
            # If tree node is null or values don't match, return False
            if not node or node.val != head.val:
                return False
            # Recur for both left and right subtree
            return dfs(node.left, head.next) or dfs(node.right, head.next)

        # Start DFS from the current root, or from left and right subtree
        return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

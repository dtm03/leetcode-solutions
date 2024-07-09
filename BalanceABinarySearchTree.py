class Solution(object):
    def balanceBST(self, root):

        def inorder(node, nodes):
            if not node:
                return
            inorder(node.left, nodes)
            nodes.append(node)
            inorder(node.right, nodes)

        def build(nodes, start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            node = nodes[mid]

            node.left = build(nodes, start, mid - 1)
            node.right = build(nodes, mid + 1, end)
            return node

        nodes = []
        inorder(root, nodes)
        n = len(nodes) - 1
        return build(nodes, 0, n)
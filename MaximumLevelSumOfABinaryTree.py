class Solution(object):
    def maxLevelSum(self, root):
        if not root:
            return 0

        q = [root]
        res = 1
        curr = 1
        max_sum = float('-inf')

        while q:
            next_level = []
            curr_sum = 0

            for node in q:
                curr_sum += node.val

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if curr_sum > max_sum:
                max_sum = curr_sum
                res = curr

            curr += 1
            q = next_level

        return res
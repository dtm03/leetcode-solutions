class Solution(object):
    def minimumRecolors(self, blocks, k):
        # Improves runtime
        if k > len(blocks):
            return 0

        res, i = float("inf"), 0
        while i + k <= len(blocks):
            res = min(res, blocks[i : i + k].count('W'))
            i += 1
        return res if res != float("inf") else 0
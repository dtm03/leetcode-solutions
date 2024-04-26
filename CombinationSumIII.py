# Backtracking

class Solution(object):
    def combinationSum3(self, k, n):
        res = []

        def backtrack(num, stack, target):
            if len(stack) == k:
                if target == 0:
                    res.append(stack)
                return

            for i in range(num + 1, 10):
                backtrack(i, stack + [i], target - i)

        backtrack(0, [], n)
        return res
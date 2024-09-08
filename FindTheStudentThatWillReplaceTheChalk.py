class Solution(object):
    def chalkReplacer(self, chalk, k):
        curr = chalk[0]
        i = 0
        k = k % sum(chalk)
        while curr <= k:
            k -= curr
            i = (i + 1) % len(chalk)
            curr = chalk[i]
        return i
# Sliding window
class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        s = [ord(c) for c in s]
        t = [ord(c) for c in t]
        l, r = 0, 0
        curr, res = 0, 0

        while r < len(s):
            curr  += abs(s[r] - t[r])

            while curr > maxCost:
                curr  -= abs(s[l] - t[l])
                l += 1

            res = max(res, r - l + 1)
            r += 1

        return res
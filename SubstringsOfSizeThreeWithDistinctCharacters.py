class Solution(object):
    def countGoodSubstrings(self, s):
        res, k = 0, 3
        i = 0
        while i + k <= len(s):
            sub = s[i : k + i]
            if len(sub) == len(set(sub)):
                res += 1
            i += 1
        return res
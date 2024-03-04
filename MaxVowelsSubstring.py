# Slide the window in order to avoid recounting vowels

class Solution(object):
    def maxVowels(self, s, k):

        vows = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        l, r = 0, k
        curr = 0

        for char in s[:k]:
            if char in vows:
                curr+=1
        res = curr

        while r < len(s):
            if s[l] in vows:
                curr-=1
            if s[r] in vows:
                curr+=1
            res = max(res, curr)
            l+=1
            r+=1

        return res
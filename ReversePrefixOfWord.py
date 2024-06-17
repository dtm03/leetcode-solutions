class Solution(object):
    def reversePrefix(self, word, ch):
        r = 0
        while r < len(word) and word[r] != ch:
            r += 1

        if r == len(word):
            return word

        res = word[0:r+1][::-1] + word[r+1:]

        return res
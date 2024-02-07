# The goal is to find the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# => Use a for-loop

class Solution(object):
    def strStr(self, haystack, needle):

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1
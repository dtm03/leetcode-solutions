# The goal is to sort the given string based on the given order and append the characters not in order at the end

class Solution(object):
    def customSortString(self, order, s):
        result = ""

        for o in order:
            for c in s:
                if o == c:
                    result += c

        for c in s:
            if c not in order:
                result += c

        return result
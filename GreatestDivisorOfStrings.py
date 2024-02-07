# The goal is to find the greatest substring that divides both strings

# The solution is to find the greatest common divisor of the lengths of the strings and check if the substring
# of that length is a divisor of both strings. If it is, then it is the greatest common divisor. If not, then we
# check the next greatest common divisor until we reach 1. If we reach 1, then there is no common divisor and we
# return an empty string.

class Solution(object):
    def gcdOfStrings(self, str1, str2):

        len1, len2 = len(str1), len(str2)

        def isDivisor(l):
            if len1 % l or len2 % l:
                return False
            f1, f2 = len1 // l, len2 // l
            return str1[:l] * f1 == str1 and str1[:l] * f2 == str2

        for l in range(min(len1, len2), 0, -1):
            if isDivisor(l):
                return str1[:l]

        return ""
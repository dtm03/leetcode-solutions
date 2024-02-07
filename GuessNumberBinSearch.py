# The goal ist to guess the number. => Use binary search and the guess API.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):

        l, h = 1, n

        while l <= h:
            m = (l + h) // 2
            c = guess(m)

            if c == 0:
                return m
            elif c == 1:
                l = m + 1
            else:
                h = m - 1

        return -1


        """
        :type n: int
        :rtype: int
        """
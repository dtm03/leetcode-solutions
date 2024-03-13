# Returns true if the prime factors of a given number only consist of 2, 3, 5

class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False

        for divisor in [2, 3, 5]:
            while n % divisor == 0:
                n //= divisor

        return n == 1

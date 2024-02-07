# The goal is to count the ones in a binary number. => Use list comprehension.

class Solution(object):
    def hammingWeight(self, n):

        b = bin(n)
        f = [bit for bit in b if bit == '1']

        return len(f)
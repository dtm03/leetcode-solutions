# The goal is to count the number of 1s in the binary representation of each number from 0 to n.

class Solution(object):
    def countBits(self, n):

        r = []

        for i in range(n+1):

            # Convert the binary to a string to use the count-Function
            r.append(str(bin(i)).count('1'))

        return r
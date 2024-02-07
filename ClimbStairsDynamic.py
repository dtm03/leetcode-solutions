# The goal is to return the number of distinct ways to climb to the top.

class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize an array to store the number of ways for each step
        ways = [0] * (n + 1)
        ways[1] = 1
        ways[2] = 2

        # Calculate the number of ways for each step from 3 to n
        for i in range(3, n + 1):
            ways[i] = ways[i - 1] + ways[i - 2]

        return ways[n]

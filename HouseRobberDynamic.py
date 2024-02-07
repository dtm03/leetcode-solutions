# Find the max of all array values without any of the values being at adjacent indices -> dynamic programming

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        # Initialize variables to keep track of the maximum values
        rob1, rob2 = 0, 0

        # Iterate through the array
        for n in nums:

            # Calculate the maximum possible considering the current house 'n'
            # This is done by comparing two choices: rob the current house (n + rob1) or skip it and keep the maximum
            # value from the previous iteration (rob2). The max function is used to choose the better option.
            temp = max(n + rob1, rob2)

            # Update rob1 and rob2 for the next iteration
            rob1 = rob2
            rob2 = temp

        # At the end of the loop, rob2 will contain the maximum amount you can rob without
        # robbing adjacent houses, so return it.
        return rob2

# Find the biggest increase between two values, so that the right one is the bigger one -> sliding window

class Solution(object):
    def maxProfit(self, prices):

    # Initialize two pointers that point to the first and second position in the array
        l, r = 0, 1

    # Initialize an int which is used to save the maximum profit (return value)
        p = 0

    # Go through the array until the right pointer has reached the end
        while r < len(prices):

    # Check whether there is an increase
            if prices[l] < prices[r]:

    # Check whether the increase is higher than the one's before
                p = max(p, prices[r] - prices[l])

    # Start a new window if there is no increase
            else:
                l = r

    # Increase the right pointer
            r+=1

        return p
# The goal in this task is to find to numbers in a sorted array (indexed at one) that add up to a given target
# -> sliding window

class Solution(object):
    def twoSum(self, n, target):

    # Initializing to pointers at each end of the array
        l, r = 0, len(n) - 1

    # Looking for the match, while the left pointer is smaller than the right one (O(n))
        while l < r:

    # Adding up the numbers at the position of the pointers
            res = n[l] + n[r]

    # Decreasing the right pointer to get a smaller number
            if res > target:
                r -= 1

    # Increasing the left pointer to get a bigger number
            elif res < target:
                l += 1

    # Returning 1-based indeces of the target-matching numbers
            else:
                return [l + 1, r + 1]


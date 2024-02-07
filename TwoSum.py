# The goal in this task is to find to numbers in an array that add up to the target -> safe numbers in hash-map (O(n))

class Solution(object):
    def twoSum(self, nums, target):

    # Initialize a hash-map
        prevMap = {}

    # Go through the nums array (i: indices, n: corresponding ints)
        for i , n in enumerate(nums):

    # Find out wich number is needed so n and diff add up to the desired target
            diff = target - n

    # Check whether the needed value is in the hash-map and return the indices
            if diff in prevMap:
                return [prevMap[diff], i]

    # If the value is not in the hash-map add it using the number as the key and the index as the value
            prevMap[n] = i
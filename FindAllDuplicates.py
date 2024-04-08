# The goal is to return an array containing all numbers that are duplicates without extra space and linear time

class Solution(object):
    def findDuplicates(self, nums):
        output = []
        for i in range(0, len(nums)):
            # Calculate the index to be inbounds
            index = abs(nums[i]) - 1
            # Check whether same index has been referenced
            if nums[index] < 0:
                # Append to output-Array
                output.append(index + 1)
            # Turn value negative
            nums[index] = -nums[index]

        return output
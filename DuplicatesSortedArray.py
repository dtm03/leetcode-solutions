# The goal is to remove duplicates from an array while maintining the order and returning the size -> Sliding with two pointers

class Solution(object):
    def removeDuplicates(self, nums):

        j = 1

        # Initializes the second pointer to start at the second element
        for i in range(1, len(nums)):

            # If the previous value is not equal it means it's unique and can be moved to the front
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]

                # Increment the second pointer
                j += 1

        return j
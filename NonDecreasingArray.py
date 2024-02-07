# Checks whether one change is sufficient to sort the array in non-decreasing order -> split into subarrays

from typing import List

class NonDecreasingArray:

    def check(self, nums: List[int]) -> bool:

        changed = False

    # Go through the array (except for the last spot)
        for i in range(len(nums) - 1):

    # Check whether the current and the following index are in order
            if nums[i] <= nums[i + 1]:
                continue

    # If that's not the case and two values were already switched return false
            if changed:
                return False

    # If the next value is bigger than the previous one change the current value to the next one
            if nums[i + 1] >= nums[i - 1]:
                nums[i] = nums[i + 1]

    # Else decrease the next one to be equal to the current one
            else:
                nums[i + 1] = nums[i]
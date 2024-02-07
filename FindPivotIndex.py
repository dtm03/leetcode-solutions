# Find the index where the sum of all the elements to the left of the index are equal to the right Sum

class Solution:
        def pivotIndex(selfself, nums: List[int]) -> int:

            total = sum(nums)
            leftSum = 0

            for i in range(len(nums)):

            # Check whether the sum of the elements to the left of the current element
            # is equal to the sum of the elements to the right of the current element
                if leftSum == total - leftSum - nums[i]:
                    return i

            # Update the left sum by adding the current element
                leftSum += nums[i]

            return -1
class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        operations = 0

        for i in range(n - 2):
            if nums[i] == 0:
                # Flip the current element and the next two elements
                for j in range(i, i + 3):
                    nums[j] = 1 - nums[j]
                operations += 1

        # Check if all elements are 1
        if all(num == 1 for num in nums):
            return operations
        else:
            return -1

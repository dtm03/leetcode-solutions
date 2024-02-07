# The goal is to remove all elements of a given value in-place and return the new length.

class Solution(object):
    def removeElement(self, nums, val):
        # Use a two-pointer approach
        i = 0  # Slow pointer

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i

'''
        2. Idee:
        Using list comprehension:
        nums = [x for x in nums if x != val]
        return len(nums)
        
        3. Idee:
        Using a while loop: (for-Loop doesn't work because of the changing length of the list)
        i = len(nums) - 1

        while i >= 0:
            if nums[i] == val:
                del nums[i]
            i -= 1

        return len(nums)
'''
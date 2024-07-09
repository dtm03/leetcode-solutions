class Solution(object):
    def removeDuplicates(self, nums):
        c = {}  # Dictionary to store counts of each element
        r = 0   # Pointer to track the position for unique elements

        for i in range(len(nums)):
            if nums[i] in c:
                c[nums[i]] += 1
            else:
                c[nums[i]] = 1

            # Only update the array if the count of the element is <= 2
            if c[nums[i]] <= 2:
                nums[r] = nums[i]
                r += 1

        # Trim the list to contain only the first 'r' elements
        return r
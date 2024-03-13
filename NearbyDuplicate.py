class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        # Create a dictionary to store the indices of elements
        num_indices = {}

        # Iterate over the array
        for i, num in enumerate(nums):
            # If the current number is already in the dictionary
            if num in num_indices:
                # Check if the difference between the current index and the stored index is less than or equal to k
                if i - num_indices[num] <= k:
                    return True
            # Update the index of the current number in the dictionary
            num_indices[num] = i

        return False
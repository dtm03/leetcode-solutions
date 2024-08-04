from collections import Counter


class Solution(object):
    def frequencySort(self, nums):
        # Step 1: Count the frequency of each element
        frequency = Counter(nums)

        # Step 2: Sort the array based on the frequency and the value itself
        nums.sort(key=lambda x: (frequency[x], -x))

        return nums
        
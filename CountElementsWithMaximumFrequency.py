class Solution(object):
    def maxFrequencyElements(self, nums):
        counts = {}

        for i in nums:
            counts[i] = counts.get(i, 0) + 1

        total_max_value = 0
        max_value = max(counts.values())

        for key, value in counts.items():
            if value == max_value:
                total_max_value += value

        return total_max_value
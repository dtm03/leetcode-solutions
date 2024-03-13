class Solution(object):
    def majorityElement(self, nums):

        candidate = None
        count = 0

        for n in nums:
            if count == 0:
                candidate = n

            count += 1 if candidate == n else -1

        return candidate
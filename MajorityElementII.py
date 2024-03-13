from collections import Counter
class Solution(object):
    def majorityElement(self, nums):

        counts = Counter(nums)
        result = []
        occ = len(nums) // 3

        for k, v in counts.items():
            if v > occ:
                result.append(k)

        return result
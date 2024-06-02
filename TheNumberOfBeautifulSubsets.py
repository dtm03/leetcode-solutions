from collections import defaultdict

# O(2^n) time | O(n) space
class Solution(object):
    def beautifulSubsets(self, nums, k):

        def helper(i, count):
            if i == len(nums):
                return 1

            res = helper(i + 1, count)
            if not count[nums[i] + k] and not count[nums[i] - k]:
                count[nums[i]] += 1
                res += helper(i + 1, count)
                count[nums[i]] -= 1
            return res

        return helper(0, defaultdict(int)) - 1



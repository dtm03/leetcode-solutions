# The approach is the same as in the consecutive 1's problem.
# The difference is k = 1 and 1 has to be subtracted from the result
# because the bit is deleted and not flipped

class Solution(object):
    def longestSubarray(self, nums):

        l = r = res = 0
        k = 1

        while r < len(nums):
            if nums[r] == 0:
                k -= 1

            if k < 0:
                if nums[l] == 0:
                    k += 1

                l += 1

            else:
                res = max(res, r - l + 1)

            r += 1

        return res - 1

# There are obviously smarter solutions than this
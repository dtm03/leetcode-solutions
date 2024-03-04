# The goal is to find the longest stretch of consecutive ones in an array
# containing 1's and 0's while beeing able to flip k bits

class Solution(object):
    def longestOnes(self, nums, k):
        l = res = 0

        for r in enumerate(nums):
            if nums[r] == 0:
                k -= 1

            if k < 0:
                if nums[l] == 0:
                    k += 1

                l += 1

            else:
                res = max(res, r - l + 1)

        return res

'''
Easier but slower solution (same logic):

class Solution(object):
    def longestOnes(self, nums, k):
        l = r = res = 0

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

        return res
        
Solution: Iterate through the array and update k if needed, change the left pointer if k is negative
'''
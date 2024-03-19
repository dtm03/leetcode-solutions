# The goal is to find out the number of subarrays in a given binary array that sum up to a given goal => Sliding window

class Solution(object):
    def numSubarraysWithSum(self, nums, goal):

        def helper(x):
            if x < 0:
                return 0
            res = 0
            l, cur = 0, 0
            for r in range(len(nums)):
                # Keeps track of the current sum
                cur += nums[r]
                while cur > x:
                    # Updates the sum and the left pointer if the current sum is bigger than the goal
                    cur -= nums[l]
                    l += 1
                # Keeps track of all the results
                res += (r - l + 1)
            return res


        # If the goal is 2 helper calculates the subarray <=2 so <=2 - <=1 becomes =2
        return helper(goal) - helper(goal - 1)
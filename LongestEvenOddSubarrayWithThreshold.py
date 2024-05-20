class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        N = len(nums)
        best = 0

        for l in range(N):
            if nums[l] % 2 != 0 or nums[l] > threshold:
                continue

            for r in range(l, N):
                good = True

                for j in range(l + 1, r + 1):
                    if nums[j] % 2 == nums[j - 1] % 2 or nums[j] > threshold:
                        good = False

                if good:
                    best = max(best, r - l + 1)

        return best

    # Much faster alternative:

    class Solution(object):
        def longestAlternatingSubarray(self, nums, threshold):
            i, t, r, n = 0, 0, 0, len(nums)
            while i < len(nums):
                if nums[i] <= threshold and nums[i] % 2 == 0 and i < n - 1:
                    if nums[i + 1] <= threshold and nums[i + 1] % 2 == 1:
                        t += 2
                        r = max(r, t)
                        i += 2
                    else:
                        t += 1
                        r = max(r, t)
                        i += 1
                        t = 0
                elif nums[i] <= threshold and nums[i] % 2 == 0 and i == n - 1:
                    t += 1
                    r = max(r, t)
                    i += 1
                else:
                    t = 0
                    r = max(r, t)
                    i += 1
            return r

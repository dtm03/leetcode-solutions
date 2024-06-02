# I understand how the result is calculated, but honestly don't understand the logic behind it.
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        odds = []
        count = 0
        for num in nums:
            if num % 2 == 1:
                odds.append(count)
                count = 0
            else:
                count += 1
        odds.append(count)

        res = 0
        for i in range(len(odds) - k):
            res += (odds[i] + 1) * (odds[i + k] + 1)
        return res
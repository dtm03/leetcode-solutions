class Solution(object):
    def increasingTriplet(self, nums):
        INF = 10 ** 20

        s1, s2 = INF, INF

        for n in nums:
            if n > s2:
                return True
            if n > s1:
                s2 = min(n, s2)
            s1 = min(n, s1)
        return False
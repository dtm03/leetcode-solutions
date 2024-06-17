from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        c = Counter(nums1)

        res = []

        for n in nums2:
            if n in c and c[n] > 0:
                res.append(n)
                c[n] -= 1

        return res
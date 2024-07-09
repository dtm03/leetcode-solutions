class Solution(object):
    def pivotArray(self, nums, pivot):
        l, h, e = [], [], []
        for n in nums:
            if n < pivot:
                l.append(n)
            elif n > pivot:
                h.append(n)
            else:
                e.append(n)

        return l + e + h
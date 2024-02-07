# Merge the arrays into nums1 and return it in non-decreasing order -> merge the arrays, sort the arrays

class Solution(object):
    def merge(self, nums1, m, nums2, n):

    # replace the corresponding zeros at the end of nums1 with the numbers of nums2
        for i in range(n):
            nums1[m+i] = nums2[i]

        nums1.sort()
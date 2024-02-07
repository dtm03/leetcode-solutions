# Given two arrays, find the difference between them -> Turn them into sets and subtract them

class Solution(object):
    def findDifference(self, nums1, nums2):

    # Turns the arrays into sets
        set1 = set(nums1)
        set2 = set(nums2)

    # Checks whether the sets are equal
        answer = [list(set1 - set2), list(set2 - set1)]

        return answer
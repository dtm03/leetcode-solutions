from bisect import bisect_left


class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        res = 0
        for i in range(len(arr1)):
            vio = False
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    vio = True
            if not vio:
                res += 1

        return res

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()  # Sort arr2 for binary search
        res = 0

        for num in arr1:
            # Find the insertion point to keep arr2 sorted
            pos = bisect_left(arr2, num)

            # Check the closest element on the left
            left_valid = (pos == 0 or abs(num - arr2[pos - 1]) > d)

            # Check the closest element on the right
            right_valid = (pos == len(arr2) or abs(num - arr2[pos]) > d)

            if left_valid and right_valid:
                res += 1

        return res
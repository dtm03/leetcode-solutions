class Solution(object):
    def duplicateZeros(self, arr):
        n = len(arr)
        zeros = arr.count(0)

        for i in range(n - 1, -1, -1):
            if i + zeros < n:
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < n:
                    arr[i + zeros] = 0

        return arr
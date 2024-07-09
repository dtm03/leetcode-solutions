class Solution(object):
    def pancakeSort(self, arr):
        res = []

        def flip(k):
            arr[:k] = arr[:k][::-1]
            res.append(k)

        for size in range(len(arr), 1, -1):
            # Find the index of the maximum number in arr[0:size]
            max_idx = arr.index(max(arr[:size]))
            if max_idx != size - 1:
                # Flip the maximum number to the front if it's not already there
                if max_idx != 0:
                    flip(max_idx + 1)
                # Flip it to its correct position
                flip(size)

        return res
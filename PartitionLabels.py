class Solution(object):
    def partitionLabels(self, s):
        # Create a dictionary to store the last index of each character
        last_index = {}
        for i, c in enumerate(s):
            last_index[c] = i

        res = []
        start = 0
        end = 0

        # Iterate through the string to determine the partitions
        for i, c in enumerate(s):
            end = max(end, last_index[c])
            # If the current index matches the end of the partition
            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res

        
# The goal is to return the Pascal's triangle up to the given number of rows.

class Solution(object):
    def generate(self, numRows):

        tri = []

        for i in range(numRows):
            row = [1]
            if tri:
                prev = tri[-1]
                # Takes the sum of each pair of elements in the previous row
                row.extend([sum(pair) for pair in zip(prev, prev[1:])])
                row.append(1)
            tri.append(row)

        return tri
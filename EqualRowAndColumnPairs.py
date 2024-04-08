from collections import defaultdict


class Solution(object):
    def equalPairs(self, grid):

        count = 0

        row_counts = defaultdict(int)

        for row in grid:
            # Tuples cuz Keys need to be hashable and Tuples are not
            row_counts[tuple(row)] += 1

        # * for transposing, zip for turning into tuples
        for col in zip(*grid):
            count += row_counts[col]

        return count


'''
Alternative without defaultdict:

class Solution(object):
    def equalPairs(self, grid):
        count = 0
        row_counts = {}

        for row in grid:
            row_key = tuple(row)
            if row_key in row_counts:
                row_counts[row_key] += 1
            else:
                row_counts[row_key] = 1

        for col in zip(*grid):
            col_key = tuple(col)
            if col_key in row_counts:
                count += row_counts[col_key]

        return count

'''
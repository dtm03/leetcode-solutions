class Solution(object):
    def largestLocal(self, grid):
        n = len(grid)
        maxLocal = [[0] * (n-2) for _ in range(n-2)]

        for i in range(n-2):
            for j in range(n-2):
                # Extract the 3x3 submatrix and find the local maximum
                local_max = max(grid[i][j], grid[i][j+1], grid[i][j+2],
                                grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                                grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2])
                maxLocal[i][j] = local_max

        return maxLocal